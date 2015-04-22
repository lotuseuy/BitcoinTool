import hashlib

m = "01000000011575f1aacac4f66f9cfecd6ea1ef272e8cb5ce33f5ae97d1fcf02cec774a82e0070000001976a914d93d248443eb1d3745891a76c0fa8a8bc86d4a3d88acffffffff01a7730100000000001976a91498dccb66b17e1efb1f0d2bba0446502f2625444488ac0000000001000000"

z = hashlib.sha256(hashlib.sha256(m.decode('hex')).digest()).digest()
z1 = z[::-1].encode('hex_codec')
z = z.encode('hex_codec')

print z
