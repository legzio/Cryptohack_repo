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
A_from_Alice = "0xd560c569b2c555e6"
x = 275463500954

A_to_Bob = pow(int(g,0),x,int(p,0))
print (hex(A_to_Bob))
#A_to_Bob = "0x2eeb6ececf62d7c8e3bab58f49a25468a1322e63e4553f9f0e10b76c7de6e53f608f7f073d41a5fdd96a798ea6064de4122a83dd2ab9cc920d7a1f15eafd244d7997cf397e9ee2ebf26c7720b12287f3f9aeae8dcf23af84607a789c8457fceee39641b920f32cf52248278708e8b8241e2b937da265599a059358868189b6f4e7dae25a1ea2423f92585bb1d8901db9fb67877cf8f743d47f2859b85ac88cb1e1ade8328b8240a331c78f85537fd394c054ba7a3872e651477d66efa2be3f2a"

B_from_Bob = "0x30cc9504a1abb716776a264b0e0a864d8fe1fbf365977da41935ce80552cd2fd33c54af8e548a01fcc2cc5ee75cd7f383635530eab1202d8041cc894834885e783ad2ccf928504ed249cdbcbbce5edffa46548072b8111271c3471a97f8d8e283245af99f3b4288cf8702695252c56ed3e4291ce78f43c37a919f4d4dcefd0a09cd588a9e8fb2f16eac32656f2dc7637a858bb64e4f7407178b000b23bff85b64cbe973daf3775d11dc2a96bc33335c0d92650a20f5b749a759030a548ca13b3"

B_to_Alice = pow(int(g,0),x,int(p,0))
print (hex(B_to_Alice))
#B_to_Alice = "0x2eeb6ececf62d7c8e3bab58f49a25468a1322e63e4553f9f0e10b76c7de6e53f608f7f073d41a5fdd96a798ea6064de4122a83dd2ab9cc920d7a1f15eafd244d7997cf397e9ee2ebf26c7720b12287f3f9aeae8dcf23af84607a789c8457fceee39641b920f32cf52248278708e8b8241e2b937da265599a059358868189b6f4e7dae25a1ea2423f92585bb1d8901db9fb67877cf8f743d47f2859b85ac88cb1e1ade8328b8240a331c78f85537fd394c054ba7a3872e651477d66efa2be3f2a"


##Intercepted from Alice: {"iv": "3e5b3a652ff42f8856ab0a8844bd9171", "encrypted_flag": "5c0e131a5f01aab7395429689b122279efd48d6ef4c15984e97e5622fad28fd8"}



shared_secret = pow(int(A_from_Alice,0),x,int(p,0))
iv = '7f3551c7b5097663463559f964af8d11'
ciphertext = '4f48dfe686f5ab96cec13337c618851d6bd7f812041b2e2980a38a2a569381eb'

print(decrypt_flag(shared_secret, iv, ciphertext))
