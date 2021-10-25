from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
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


g = "0x2"
p = "0xde26ab651b92a129"
A = "0x5cf7b6f5f1b5dccc"
B = "0xcdb94eb898f33f41"
x = 0


for i in range(1,int(p,0)):
    A_temp = pow(int(g,0),i,int(p,0))
    if (A_temp==int(A,0)):
        x = i
        break


#A_to_Bob = pow(int(g,0),x,int(p,0))
#print (hex(A_to_Bob))




shared_secret = pow(int(A,0),x,int(p,0))
iv = 'f1dbf7b396fcf3dbe7d75d006b7ba16d'
ciphertext = '0e1c229ee725c5fafd531e6d0ebebe4269367131b8ec8a271be11f70ca298935'

print(decrypt_flag(shared_secret, iv, ciphertext))

#Intercepted from Alice: {"p": "0xde26ab651b92a129", "g": "0x2", "A": "0x5cf7b6f5f1b5dccc"}
#Intercepted from Bob: {"B": "0xcdb94eb898f33f41"}
#Intercepted from Alice: {"iv": "f1dbf7b396fcf3dbe7d75d006b7ba16d", "encrypted_flag": "0e1c229ee725c5fafd531e6d0ebebe4269367131b8ec8a271be11f70ca298935"}
