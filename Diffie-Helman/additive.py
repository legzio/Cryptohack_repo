from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

#Intercepted from Alice: 
from_alice = {"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0x02", "A": "0xbb5d2b48b6e4fcade88af85c85cfafdba013d17ee589cf5c2178f8dd7110d07bd53fcdafeb0b1cdfe8d2fc2fdbc79c21aed9dac8ace4e470788646ec6d309c56dba8859e690024d41d87708baa95b1f361dec486e84fc8383d9db221ecc875de27745d6340e5b981360e53b0132bcb029267840e8ebd5a81487063fdd678a1116a59c9b0d44d008c5e9b47767170143b7bc3618c2fb41ddeeb4e45f8b138d5088c0e55fb7451cd56a917c1e5a414c1637697181f3d6506a4192ab89de0e4cba5"}
#Intercepted from Bob: 
from_bob = {"B": "0x1b0b655c7fac746b158f567215d376df013c7ac14c1a405972c5e0432914015627ce154079917fba52680146039caa963d072afe1f79da6d018455494aa9fa8112bbad40a51de54499a021f4ca27ed7f9419862416c40f0f2d9205fb306eb7ec4337ff1ef040d1ed4ac78798f7c78451c0cf160f260ba41a983f8a7557c06564e42f32a575a4aba17e2a774e997bc12e2edf0e11a98050dd11299bb5c29f568386f37b80301b019830e9ea87c603578be624de08928122d905896f6f6a26d36d"}
#Intercepted from Alice: 
msg = {"iv": "19d1777f8ef3a0e0ecdf9b0889da0077", "encrypted": "eb1f79afb85902cfbef66438b6a128a20c4113356f22b51ea2b8a11ab9e69baa208ea155ebc842ad0691f4cb3471380a"}



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

b = int(from_bob["B"], base=16)/int(from_alice["g"], base=16)        
B = int(from_bob["B"], base=16)
p = int(from_alice["p"], base=16)

shared_secret = pow(B,b,p)
iv = msg["iv"]
ciphertext = msg["encrypted"]

print(decrypt_flag(shared_secret, iv, ciphertext))