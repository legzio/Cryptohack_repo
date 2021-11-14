from base64 import b64encode, b64decode

string = 'Litwo! Ojczyzno moja. Ty jestes jak zdrowie.'.encode()

secret = b64encode(string)

print (secret)

plain = b64decode(secret)

print (plain)
