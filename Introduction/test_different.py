from Crypto.Util.number import bytes_to_long, inverse, long_to_bytes
from base64 import b64decode

key = b'MFswDQYJKoZIhvcNAQEBBQADSgAwRwJATKIe3jfj1qY7zuX5Eg0JifAUOq6RUwLzRuiru4QKcvtW0Uh1KMp1GVt4'
n_int = b64decode(key)

print(bytes_to_long(n_int))

