from Crypto.Util.number import bytes_to_long, long_to_bytes
from binascii import unhexlify

cryptotext = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
data = unhexlify(cryptotext)
for i in range(256):
    data1 = b''
    for n in (data):
        data1 += bytes([n^i])
    if data1.startswith(b"crypto"):
        print (data1)
