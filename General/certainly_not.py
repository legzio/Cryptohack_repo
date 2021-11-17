from Crypto.PublicKey import RSA
from asn1crypto.x509 import Certificate
from base64 import b64decode, b64encode
from binascii import a2b_base64
from ssl import DER_cert_to_PEM_cert

f = open('./General/2048b-rsa-example-cert.der', 'rb')

cert = Certificate.load(f.read())
key = cert.public_key.native['public_key']['modulus']

print(key)