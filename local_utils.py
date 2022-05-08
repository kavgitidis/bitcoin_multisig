import requests
from bitcoinutils.keys import PrivateKey, P2pkhAddress
from bitcoinutils.proxy import NodeProxy
from bitcoinutils.script import Script
from bitcoinutils.setup import setup
from bitcoinutils.transactions import Transaction, TxInput, TxOutput
from bitcoinutils.utils import to_satoshis


class Mom:
    def __init__(self, net, rpcuser, rpcpass):
        setup(net)
        self.rpcuser = rpcuser
        self.rpcpass = rpcpass

    def init_proxy(self) -> NodeProxy:
        try:
            return NodeProxy(rpcuser=self.rpcuser, rpcpassword=self.rpcpass).get_proxy()
        except:
            pass

    def create_wallet(self, wallet_name: str):
        proxy = self.init_proxy()
        wallet = proxy.batch_([["createwallet", f"{wallet_name}"]])
        return wallet

    def get_new_address(self, add_name, add_type):
        proxy = self.init_proxy()
        addr = proxy.batch_([["getnewaddress", f"{add_name}", f"{add_type}"]])[0]
        privk = proxy.batch_([["dumpprivkey", f"{addr}"]])[0]
        pubk = PrivateKey(privk).get_public_key().to_hex()

        return {"Name": add_name,
                "Address": addr,
                "Private Key": privk,
                "Public Key": pubk,
                "Type": add_type}

    @staticmethod
    def get_public_from_private(private_key):
        return PrivateKey(private_key).get_public_key().to_hex()

    def generate_to_address(self, blocks: int, address: str):
        proxy = self.init_proxy()
        res = proxy.batch_([["generatetoaddress", blocks, f"{address}"]])[0]
        return res

    def send_to_address(self, address: str, amount: int):
        proxy = self.init_proxy()
        tx = proxy.batch_([["sendtoaddress", f"{address}", amount]])[0]
        return tx

    def get_utxos(self, address: str):
        proxy = self.init_proxy()
        utxos = proxy.batch_([["scantxoutset", "start", [f"addr({address})"]]])
        if utxos[0]['success']:
            return utxos[0]['unspents']
        else:
            return False

    @staticmethod
    def calculate_fees(utxos):
        # use API to get the fees like in testnet
        url = 'https://api.blockcypher.com/v1/btc/test3'
        resp = requests.get(url)
        medium_fee_per_kb = resp.json()['medium_fee_per_kb']
        tx_size = len(utxos) * 180 + 34 + 10 + len(utxos)
        return to_satoshis(tx_size * medium_fee_per_kb / (1024 * 10 ** 8))

    def create_multisig_address(self, addresses, m):
        proxy = self.init_proxy()
        # I have no idea why addmultisig always produces an error when hashing the redeem script
        multisig = proxy.batch_([["createmultisig", int(m), [str(i) for i in addresses]]])
        return multisig

    @staticmethod
    def create_raw_multisig_tx(utxos, address, amount, fees):
        txin = [TxInput(tx['txid'], tx['vout']) for tx in utxos]
        txout = TxOutput(to_satoshis(amount) - fees, P2pkhAddress(address).to_script_pub_key())
        raw_tx = Transaction(txin, [txout])
        return raw_tx, txin

    @staticmethod
    def sign_raw_multisig_tx(priv_keys, txin_list, tx, pub_keys):
        for i, txin in enumerate(txin_list):
            redeem_script = Script(['OP_2', pub_keys[0], pub_keys[1], pub_keys[2],
                                    'OP_3', 'OP_CHECKMULTISIG'])

            sigs = [PrivateKey(pk).sign_input(tx, i, redeem_script) for pk in priv_keys]
            txin.script_sig = Script(
                ['OP_0', sigs[0], sigs[1], redeem_script.to_hex()])

    def validate_transaction(self, tx):
        proxy = self.init_proxy()
        return proxy.testmempoolaccept([tx])

    def send_transaction(self, tx):
        proxy = self.init_proxy()
        proxy.sendrawtransaction(tx)
