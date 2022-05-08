import sys
from pprint import pprint

import click

from local_utils import Mom


@click.command()
@click.option('--pk1', default=None, help='Private Key 1')
@click.option('--pk2', default=None, help='Private Key 2')
@click.option('--pub', default=None, help='Public Key')
@click.option('--p2pkh', default=None, help='Public Key address to sends the funds to')
@click.option('--multisig', default=None, help='Multisig Address to get the funds from')
@click.option('--rpcuser', default="admin", help='Rpcuser')
@click.option('--rpcpass', default="admin", help='Rpcpassword')
@click.option('--network', default="regtest", help='Bitcoin Network')
def main(*args, **kwargs):
    click.echo(f"Private Keys Provided: {kwargs['pk1']} | {kwargs['pk2']}")
    click.echo(f"Public Key Provided: {kwargs['pub']}")
    click.echo(f"Multisig Address: {kwargs['multisig']}")
    click.echo(f"P2PKH Address: {kwargs['p2pkh']}")
    mom = Mom(net=kwargs['network'], rpcuser=kwargs['rpcuser'], rpcpass=kwargs['rpcpass'])

    # Getting public keys from private keys provided
    pub2 = mom.get_public_from_private(kwargs['pk1'])
    pub3 = mom.get_public_from_private(kwargs['pk2'])

    utxos = mom.get_utxos(kwargs['multisig'])
    if utxos != False:
        pprint(f"Available UTXOS: {utxos}")
        # calculate the total amount to pay (donate them all!)
        total_amount = int()
        for i in utxos:
            total_amount = total_amount + i['amount']
        pprint(f"Total amount to pay: {total_amount} BTC")
    else:
        print("No funds available in this address")
        sys.exit(0)
    fees = mom.calculate_fees(utxos)
    print('Transaction fees in satoshis:', fees)
    raw_tx, txin_list = mom.create_raw_multisig_tx(utxos, kwargs['p2pkh'], total_amount, fees)
    # print(raw_tx.serialize())
    pprint(f"Raw unsigned transaction: {raw_tx.serialize()}")
    mom.sign_raw_multisig_tx([kwargs['pk1'], kwargs['pk2']], txin_list, raw_tx,
                             [pub2, pub3, kwargs['pub']])
    pprint(f"Raw Signed transaction: {raw_tx.serialize()}")
    pprint(f"Signed transaction ID: {raw_tx.get_txid()}")
    # pprint(f"Signed transaction: {raw_tx}")
    signed_tx = raw_tx.serialize()
    res = mom.validate_transaction(signed_tx)

    if res[0]['allowed']:
        print("Transaction is valid!")
        txid = mom.send_transaction(signed_tx)
        print(f"Sent transaction to the blockchain!")
    else:
        print(f"Transaction is not valid, Reason:{res[0]['reject-reason']}")


if __name__ == '__main__':
    main()
