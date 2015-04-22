#### Tool ini digunakan untuk parsing transaksi raw pada bitcoin
#### untuk membagi komponenen - komponen pada transaksi tersebut 
#### untuk digunakan pada perhitungan matematikan ECDSA
#### output :
#### 1. signed tx : full raw tx
#### 2. unsigned tx
#### 3. r,s pair pada signature
#### 4. pubkey
#### 5. z : hash dari unsigned tx
#### OK bisa digunkanan####

#### tool ini membutuhkan txnUtils dan keyUtils dari https://github.com/shirriff/bitcoin-code

import hashlib
import txnUtils
import keyUtils

tx = "0100000001f2068914e2fea859cacd8df990daf4008f11296b3cb953794051147a265d850a000000008b483045022043784344e1e0cb498c1d73b4cee970fb0f9adf38b7891d0b1310fdb9cbc23929022100a734f4e97a05bd169a9f0eb296fc841fa57f8753db09869f8f6f8cc1232616d4014104d6597d465408e6e11264c116dd98b539740e802dc756d7eb88741696e20dfe7d3588695d2e7ad23cbf0aa056d42afada63036d66a1d9b97070dd6bc0c87ceb0dffffffff0100b864d9450000001976a9142df31a60b02cce392822c9a87198753578ef7de888ac00000000"

m = txnUtils.parseTxn(tx)
e = txnUtils.getSignableTxn(m)
z = hashlib.sha256(hashlib.sha256(e.decode('hex')).digest()).digest()
z = z.encode('hex_codec')
s = keyUtils.derSigToHexSig(m[1][:-2])
pub =  m[2]

print 'Signed TX is :', tx
print 'Signature (r, s pair) is :', s
print 'Public Key is :', pub
print ""
print "##################"
print ""
print 'Unsigned TX is :', e
print 'hash of message (z value) is :', z
