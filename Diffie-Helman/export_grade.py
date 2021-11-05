from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from sympy.ntheory import discrete_log
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')


#Intercepted from Alice: {"supported": ["DH1536", "DH1024", "DH512", "DH256", "DH128", "DH64"]}
#Send to Bob: {"supported": ["DH64"]}
#Intercepted from Bob: {"chosen": "DH64"}
#Send to Alice: {"chosen": "DH64"}
#Intercepted from Alice: {"p": "0xde26ab651b92a129", "g": "0x2", "A": "0xaad7372857929c14"}
#Intercepted from Bob: {"B": "0xb32c45b20a6f0fd8"}
#Intercepted from Alice: {"iv": "7058dcd3293ff43b9da8155c2d737400", "encrypted_flag": "f7234438f057b4ae550009fe811687013d45414f28983cb7c69dcd04ee5abe55"}

p = "0xde26ab651b92a129"
g = "0x2"
A = "0xaad7372857929c14"
B = "0xb32c45b20a6f0fd8"

# B = g^b mod p  -->  b = log g (B) mod p
# secret = A^b mod p

# discrete_log(p,B,g) - (modulo, logarithm_from, base)

b = discrete_log(int(p, base=16),int(B, base=16),int(g, base=16))

shared_secret = pow(int(A,base=16),b,int(p, base=16))

print(shared_secret)

iv = '7058dcd3293ff43b9da8155c2d737400'
ciphertext = 'f7234438f057b4ae550009fe811687013d45414f28983cb7c69dcd04ee5abe55'

print(decrypt_flag(shared_secret, iv, ciphertext))
