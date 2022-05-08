# bitcoin_multisig
Create a 2-3 multisig bitcoin address and send some funds from it to a p2pkh.
run the commands before doing anything if you have a previous regtest setup!
bitcoin-cli stop
rm -r .bitcoin/regtest
bitcoind

Bitcoin conf:
regtest=1
server=1
rpcuser=admin
rpcpassword=admin

[regtest]
maxtxfee=20
fallbackfee=1

Run the launch_me_first.py file and get some public keys from the output from the first script and send some funds to the multisig address!
python launch_me_first.py

Example output:
[{'name': 'myfirstwallet', 'warning': '-fallbackfee is set very high! This is the transaction fee you may pay when fee estimates are not available.\n-maxtxfee is set very high! Fees this large could be paid on a single transaction.'}]
{'Address': 'bcrt1qdeccklfcqcvw5mkjugllx6a2t0xwsxz2xytlml',
 'Name': '1st Address',
 'Private Key': 'cRe4XSb2dMyB56xV6M8iVkPrwCiEXP9TmwnLaL46d2xVWtmKogte',
 'Public Key': '02c24c68e30b17da30f1017dbb77e9a3b22413635e61fd846380d1c1943c71967e',
 'Type': 'bech32'}
{'Address': 'bcrt1qgun0cmqe64km7qtdae5eycczh24uaz8rqhpyfq',
 'Name': '2nd Address',
 'Private Key': 'cNBmsEUxPxcNDSC8mB7FTMvxNqgjoFQS47gWkACzGnrw2q2PBfpT',
 'Public Key': '02d2f94d06d54fc82d6a4e68519046496a2a11376206d9c1b4f05ea60b2cfd8319',
 'Type': 'bech32'}
{'Address': 'mzuQ6G28ZkHCtdAj28G2Lzv5Q1MgHf1Txf',
 'Name': '3rd Address',
 'Private Key': 'cUFCbUo9sz39JrZJEmV55exCdxqYkY66m2LtbbGHidRyDULF2Zta',
 'Public Key': '037aa2e81e10f221676ed97b67437a9150178e1d33ed06247c16474027e4d52d4f',
 'Type': 'legacy'}
[{'address': '2NEg9ftDwvnPWLfxoGPKDboJyhn8WGvwQTV',
  'descriptor': 'sh(multi(2,02c24c68e30b17da30f1017dbb77e9a3b22413635e61fd846380d1c1943c71967e,02d2f94d06d54fc82d6a4e68519046496a2a11376206d9c1b4f05ea60b2cfd8319,037aa2e81e10f221676ed97b67437a9150178e1d33ed06247c16474027e4d52d4f))#veqvjpjq',
  'redeemScript': '522102c24c68e30b17da30f1017dbb77e9a3b22413635e61fd846380d1c1943c71967e2102d2f94d06d54fc82d6a4e68519046496a2a11376206d9c1b4f05ea60b2cfd831921037aa2e81e10f221676ed97b67437a9150178e1d33ed06247c16474027e4d52d4f53ae'}]
'Total amount to pay: 69.00000000 BTC'
Transaction fees in satoshis: 29898
('Raw unsigned transaction: '
 '0200000003957f384b0bfa57c09be2b2e04721b284401ac6d2631db3ee6b2162a380b765bb0000000000ffffffffd87e78ebda4de6d14b98e4078024ace30e8927f37258801aeafce0062af748530000000000fffffffff130b90659608ae56e6f6aa741cb5cf369619bcb3a26ebe327e37a2dd3e138430000000000ffffffff013630459b010000001976a914d4a91333e990037e479a53b1db73e02b0e4aa1f488ac00000000')
('Raw Signed transaction: '
 '0200000003957f384b0bfa57c09be2b2e04721b284401ac6d2631db3ee6b2162a380b765bb00000000fdfd0000483045022100b57288926816dee30b4b03815764087f7cf1df9ce6dc523d529de3b15f6dcd27022003c0bc886e0dc069cfbacf29a3c3cea24c017470b6ce50763f358fb1599299a101473044022029072cece0a7e043af7fe8e816daebaa1b324572e3c5d62383c8a96be6f4021e02203670e1562d3c6ae8a0fe0268a58248d47436d15240e3b9259ed01ee078cb2a89014c69522102c24c68e30b17da30f1017dbb77e9a3b22413635e61fd846380d1c1943c71967e2102d2f94d06d54fc82d6a4e68519046496a2a11376206d9c1b4f05ea60b2cfd831921037aa2e81e10f221676ed97b67437a9150178e1d33ed06247c16474027e4d52d4f53aeffffffffd87e78ebda4de6d14b98e4078024ace30e8927f37258801aeafce0062af7485300000000fdfd000047304402205a6c2d80de6fd8b38064fd42cbfdad844eb9fdb5e532a9f0c9b37bb5fe731482022059fc35bd4c71faba4e6ed9adf07c5029a87bb1c4fd95c47c9d81bb2f1edf47c6014830450221008de82d50d2f9fcd9d92060f8578cea7d53cd1e742671034e5f38b17a0bee94f102207c310aed0554e45e166e72589de317da5fe4ad97797bd0044e314eb748c9345f014c69522102c24c68e30b17da30f1017dbb77e9a3b22413635e61fd846380d1c1943c71967e2102d2f94d06d54fc82d6a4e68519046496a2a11376206d9c1b4f05ea60b2cfd831921037aa2e81e10f221676ed97b67437a9150178e1d33ed06247c16474027e4d52d4f53aefffffffff130b90659608ae56e6f6aa741cb5cf369619bcb3a26ebe327e37a2dd3e1384300000000fdfd0000483045022100b34f4168e76256c01f1ff1d7801c614eb98f547944edaec9fcfd8ee9a27fa6aa02202b3f5f745f13f4910823608c6070bd77a1ca4d932f2ae0f1c4b9c9c99fc772fc01473044022029a9c25da470c42debf43011e9593e5d8b9c4db808aa59258f4a728dadadd4c40220249899b2cc05562e74fe2f4636febc51162f5e6d49fb7c99103dda59b883e128014c69522102c24c68e30b17da30f1017dbb77e9a3b22413635e61fd846380d1c1943c71967e2102d2f94d06d54fc82d6a4e68519046496a2a11376206d9c1b4f05ea60b2cfd831921037aa2e81e10f221676ed97b67437a9150178e1d33ed06247c16474027e4d52d4f53aeffffffff013630459b010000001976a914d4a91333e990037e479a53b1db73e02b0e4aa1f488ac00000000')
('Signed Transaction ID: '
 '659c1259ac35c9eb22d0892ac28ead5855fffd9c3f275849de63448b27da31fe')


Use them for the first script, it should output the same multisig address again:
python script1.py --pub1=02c24c68e30b17da30f1017dbb77e9a3b22413635e61fd846380d1c1943c71967e --pub2=02d2f94d06d54fc82d6a4e68519046496a2a11376206d9c1b4f05ea60b2cfd8319 --pub3=037aa2e81e10f221676ed97b67437a9150178e1d33ed06247c16474027e4d52d4f

Example output:
Public Keys Provided: 02c24c68e30b17da30f1017dbb77e9a3b22413635e61fd846380d1c1943c71967e | 02d2f94d06d54fc82d6a4e68519046496a2a11376206d9c1b4f05ea60b2cfd8319 | 037aa2e81e10f221676ed97b67437a9150178e1d33ed06247c16474027e4d52d4f
Multisig Address: 2NEg9ftDwvnPWLfxoGPKDboJyhn8WGvwQTV
[{'address': '2NEg9ftDwvnPWLfxoGPKDboJyhn8WGvwQTV',
  'descriptor': 'sh(multi(2,02c24c68e30b17da30f1017dbb77e9a3b22413635e61fd846380d1c1943c71967e,02d2f94d06d54fc82d6a4e68519046496a2a11376206d9c1b4f05ea60b2cfd8319,037aa2e81e10f221676ed97b67437a9150178e1d33ed06247c16474027e4d52d4f))#veqvjpjq',
  'redeemScript': '522102c24c68e30b17da30f1017dbb77e9a3b22413635e61fd846380d1c1943c71967e2102d2f94d06d54fc82d6a4e68519046496a2a11376206d9c1b4f05ea60b2cfd831921037aa2e81e10f221676ed97b67437a9150178e1d33ed06247c16474027e4d52d4f53ae'}]

Use them again along with the private keys and multisig address to test the second script:
python script2.py --pk1=cRe4XSb2dMyB56xV6M8iVkPrwCiEXP9TmwnLaL46d2xVWtmKogte --pk2=cNBmsEUxPxcNDSC8mB7FTMvxNqgjoFQS47gWkACzGnrw2q2PBfpT --pub=037aa2e81e10f221676ed97b67437a9150178e1d33ed06247c16474027e4d52d4f --p2pkh=mzuQ6G28ZkHCtdAj28G2Lzv5Q1MgHf1Txf --multisig=2NEg9ftDwvnPWLfxoGPKDboJyhn8WGvwQTV
Example output:
Private Keys Provided: cRe4XSb2dMyB56xV6M8iVkPrwCiEXP9TmwnLaL46d2xVWtmKogte | cNBmsEUxPxcNDSC8mB7FTMvxNqgjoFQS47gWkACzGnrw2q2PBfpT
Public Key Provided: 037aa2e81e10f221676ed97b67437a9150178e1d33ed06247c16474027e4d52d4f
Multisig Address: 2NEg9ftDwvnPWLfxoGPKDboJyhn8WGvwQTV
P2PKH Address: mzuQ6G28ZkHCtdAj28G2Lzv5Q1MgHf1Txf
("Available UTXOS: [{'txid': "
 "'bb65b780a362216beeb31d63d2c61a4084b22147e0b2e29bc057fa0b4b387f95', 'vout': "
 "0, 'scriptPubKey': 'a914eb116fc87a120aa2bdbd70d6c80a161c7c6943b987', 'desc': "
 "'addr(2NEg9ftDwvnPWLfxoGPKDboJyhn8WGvwQTV)#9dh4mcda', 'amount': "
 "Decimal('12.00000000'), 'height': 124}, {'txid': "
 "'5348f72a06e0fcea1a805872f327890ee3ac248007e4984bd1e64ddaeb787ed8', 'vout': "
 "0, 'scriptPubKey': 'a914eb116fc87a120aa2bdbd70d6c80a161c7c6943b987', 'desc': "
 "'addr(2NEg9ftDwvnPWLfxoGPKDboJyhn8WGvwQTV)#9dh4mcda', 'amount': "
 "Decimal('23.00000000'), 'height': 124}, {'txid': "
 "'4338e1d32d7ae327e3eb263acb9b6169f35ccb41a76a6f6ee58a605906b930f1', 'vout': "
 "0, 'scriptPubKey': 'a914eb116fc87a120aa2bdbd70d6c80a161c7c6943b987', 'desc': "
 "'addr(2NEg9ftDwvnPWLfxoGPKDboJyhn8WGvwQTV)#9dh4mcda', 'amount': "
 "Decimal('34.00000000'), 'height': 124}]")
'Total amount to pay: 69.00000000 BTC'
Transaction fees in satoshis: 29654
('Raw unsigned transaction: '
 '0200000003957f384b0bfa57c09be2b2e04721b284401ac6d2631db3ee6b2162a380b765bb0000000000ffffffffd87e78ebda4de6d14b98e4078024ace30e8927f37258801aeafce0062af748530000000000fffffffff130b90659608ae56e6f6aa741cb5cf369619bcb3a26ebe327e37a2dd3e138430000000000ffffffff012a31459b010000001976a914d4a91333e990037e479a53b1db73e02b0e4aa1f488ac00000000')
('Raw Signed transaction: '
 '0200000003957f384b0bfa57c09be2b2e04721b284401ac6d2631db3ee6b2162a380b765bb00000000fdfd000048304502210095be646c1ef7d06e3fa864c6346ce784583f847628b025eb23ac5df2b6f1485a022072eea57a2e61d77b5b2923e6a07046bfcb08a36a69bd6b58b47e8945de49909101473044022028202f443712b035c5f582d25564d301d344c212d82f405b4042659605ee9a00022004c01930a7d15e814772ca0efc8da1a309ed252c770dd3573a73bc8672a5d548014c69522102c24c68e30b17da30f1017dbb77e9a3b22413635e61fd846380d1c1943c71967e2102d2f94d06d54fc82d6a4e68519046496a2a11376206d9c1b4f05ea60b2cfd831921037aa2e81e10f221676ed97b67437a9150178e1d33ed06247c16474027e4d52d4f53aeffffffffd87e78ebda4de6d14b98e4078024ace30e8927f37258801aeafce0062af7485300000000fdfd000047304402200f46029b678de51be46321e767fd3b22e33753b3dce42e9931ce6c3c2da7381302203953ad2e132cddf3ba381b5b89d855d6b640214d377710d27f7d7c1aac70dbd201483045022100e8430dc2bd75fc7d791c6794aa759e3931a400f9217b281f41935193d60cdf5f0220552cbe388e2c1f028c14e484e000514748fdfd891c252b0f07dac9ea3c9f47a4014c69522102c24c68e30b17da30f1017dbb77e9a3b22413635e61fd846380d1c1943c71967e2102d2f94d06d54fc82d6a4e68519046496a2a11376206d9c1b4f05ea60b2cfd831921037aa2e81e10f221676ed97b67437a9150178e1d33ed06247c16474027e4d52d4f53aefffffffff130b90659608ae56e6f6aa741cb5cf369619bcb3a26ebe327e37a2dd3e1384300000000fdfd000047304402201569ff0332092866562202b02c55aee94c2eb2fa5ff260d6aaca1960a7cdaba9022022344a020e3c1bbd3f7fa9d8135c75b4c669609b0773e9d60d55d78ae194b21d014830450221008de9441fbe63208dcf3d6467f15b9c3f842a2d140b4699b7d46f5f8010e2324a02200d47eab91496dfc7d098af8ffed8d1358f1e14cec85a0460609a7026b5471c22014c69522102c24c68e30b17da30f1017dbb77e9a3b22413635e61fd846380d1c1943c71967e2102d2f94d06d54fc82d6a4e68519046496a2a11376206d9c1b4f05ea60b2cfd831921037aa2e81e10f221676ed97b67437a9150178e1d33ed06247c16474027e4d52d4f53aeffffffff012a31459b010000001976a914d4a91333e990037e479a53b1db73e02b0e4aa1f488ac00000000')
('Signed transaction ID: '
 '4b8014bbcef72f73d7f8d508fbc95f307a46fd027bd40cfecf7b510fdcb63b3f')
Transaction is valid!
Sent transaction to the blockchain!

Congratulations you are now ~69 BTC richer, nice!
