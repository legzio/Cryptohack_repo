from Crypto.Cipher import AES
import hashlib
import random
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes

FLAG = " "
ciphertext = 'c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66'


# @chal.route('/passwords_as_keys/decrypt/<ciphertext>/<password_hash>/')
# def decrypt(ciphertext, password_hash):
    # ciphertext = bytes.fromhex(ciphertext)
    # key = bytes.fromhex(password_hash)
    # key = password_hash

    # cipher = AES.new(key, AES.MODE_ECB)
    # try:
        # decrypted = cipher.decrypt(ciphertext)
    # except ValueError as e:
        # return {"error": str(e)}

    # return {"plaintext": decrypted.hex()}
    # return decrypted.hex()


# @chal.route('/passwords_as_keys/encrypt_flag/')
# def encrypt_flag():
    # cipher = AES.new(KEY, AES.MODE_ECB)
    # encrypted = cipher.encrypt(FLAG.encode())
# 
    # return {"ciphertext": encrypted.hex()}
    

# /usr/share/dict/words from
# https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words
with open("./Symmetric_Ciphers/AES/words") as f:
    words = [w.strip() for w in f.readlines()]

z = len(words)
for i in range(z):
    keyword = words[i]
    # print(keyword)
    key = hashlib.md5(keyword.encode()).digest()
    # print(key)
    ciphertext1 = bytes.fromhex(ciphertext)
    # plain = decrypt(ciphertext,key)
    cipher = AES.new(key, AES.MODE_ECB)
    # try:    
    decrypted = cipher.decrypt(ciphertext1)
    text = decrypted.hex()
    plain = long_to_bytes(int(text,base=16))
    # if plain[0:5] == "crypto":
    print(plain)
    # except:
        # w=1   

#  in the output there is flag: 
#  b'crypto{k3y5__r__n07__p455w0rdz?}'      


