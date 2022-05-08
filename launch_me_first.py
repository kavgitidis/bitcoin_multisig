import sys
from pprint import pprint

from local_utils import Mom

mom = Mom(net="regtest", rpcuser="admin", rpcpass="admin")

print(mom.create_wallet("myfirstwallet"))
add1 = mom.get_new_address("1st Address", "bech32")
add2 = mom.get_new_address("2nd Address", "bech32")
add3 = mom.get_new_address("3rd Address", "legacy")
pprint(add1)
pprint(add2)
pprint(add3)
mom.generate_to_address(123, add1['Address'])

multisig = mom.create_multisig_address([add1['Public Key'], add2['Public Key'], add3['Public Key']], 2)
multisig_add = multisig[0]['address']
pprint(multisig)
# Send some fund to the multisig address
mom.send_to_address(f"{multisig_add}", 12)
mom.send_to_address(f"{multisig_add}", 23)
mom.send_to_address(f"{multisig_add}", 34)
mom.generate_to_address(1, add1['Address'])
utxos = mom.get_utxos(multisig_add)
if utxos != False:
    total_amount = int()
    for i in utxos:
        total_amount = total_amount + i['amount']
    pprint(f"Total amount to pay: {total_amount} BTC")
else:
    print("No funds available in this address")
    sys.exit(0)
fees = mom.calculate_fees(utxos)
print('Transaction fees in satoshis:', fees)

raw_tx, txin_list = mom.create_raw_multisig_tx(utxos, add3['Address'], total_amount, fees)
pprint(f"Raw unsigned transaction: {raw_tx.serialize()}")

mom.sign_raw_multisig_tx([add1['Private Key'], add2['Private Key']], txin_list, raw_tx,
                         [add1['Public Key'], add2['Public Key'], add3['Public Key']])
pprint(f"Raw Signed transaction: {raw_tx.serialize()}")
pprint(f"Signed Transaction ID: {raw_tx.get_txid()}")
signed_tx = raw_tx.serialize()
res = mom.validate_transaction(signed_tx)

if res[0]['allowed']:
    # DO NOT UNCOMMENT IF YOU WANT TO FUND THE SEGWIT ADDRESS
    # txid = mom.send_transaction(signed_tx)
    # print(f"Sent transaction to the blockchain!")
    pass
else:
    print(f"Transaction is not valid, Reason:{res[0]['reject-reason']}")
