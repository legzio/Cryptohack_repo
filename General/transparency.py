from Crypto.PublicKey import RSA

f = open('./General/transparency.pem', 'r')


key = RSA.importKey(f.read())

print(key)