from Crypto.Util.number import bytes_to_long, long_to_bytes
from binascii import unhexlify


cryptotext = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
data = unhexlify(cryptotext)

mask = 'crypto{'.encode()


print(cryptotext)
print(data)
print(mask)


data1 = b''
for b1,b2 in zip(data[:7],mask):
        # print(data[i], " , ", mask[i], " , ", (data[i]^mask[i]).decode('utf-8'))
    data1 += bytes([b1 ^ b2])
print(data1)

# above code gave partial key:
# b'myXORke'
# probably missed letter is "y", and key is repeated as long is encrypted message:

key_part = b'myXORkey'      # key is long 8 chars

data_long = int(len(data))
key = key_part * int(((data_long - 8)/8)+1)
key = key + key[:((data_long - 8)%8)]
data1 = b''
for b1,b2 in zip(data,key):    
        # print(data[i], " , ", mask[i], " , ", (data[i]^mask[i]).decode('utf-8'))
    data1 += bytes([b1 ^ b2])
print(data1.decode())

result = int(cryptotext, base=16)
key_dig = int()
