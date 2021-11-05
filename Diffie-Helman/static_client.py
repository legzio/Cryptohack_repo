from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


#A = g^a mod p

p = "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff"
g = "0x02"
A = "0xf60aca7dbe32c1bb2fa40f5056712d26df16cbdd09e02dee7443f0ade200adc38986756c8c6ad5ad22581d3b3e1ef83e1174208a1b49e01004d071e3a3f3753fd3f8be70ab0e77fc31054e1b2a1bcb4efae6b4ee7103a349d2a6f9d10ae68750fb3a5d0f1c779d3a92ed50674eed27eff8870a2c1e80432654b46f85bb2327ab9fa4ff66d150cde7f2292e616c6adc6adc402491e819ff3a7de6ff8a8bf51933cafd4446109f42c7e2ff298cdefc1a3beec299cf499b4a4aaba8995a255aa762"

# from  Bob:
#B = g^b mod p

# secret = A^b mod p = B^a mod p
# it seems that Bob is reusing the same b, because in several responses he send the same B:
B = "0x8d79b69390f639501d81bdce911ec9defb0e93d421c02958c8c8dd4e245e61ae861ef9d32aa85dfec628d4046c403199297d6e17f0c9555137b5e8555eb941e8dcfd2fe5e68eecffeb66c6b0de91eb8cf2fd0c0f3f47e0c89779276fa7138e138793020c6b8f834be20a16237900c108f23f872a5f693ca3f93c3fd5a853dfd69518eb4bab9ac2a004d3a11fb21307149e8f2e1d8e1d7c85d604aa0bee335eade60f191f74ee165cd4baa067b96385aa89cbc7722e7426522381fc94ebfa8ef0"

# if Bob calculate B as g^b mod p and secret as A^b mod p - try to send him as g value the A. He should send as "his B" the secret value..
#Intercepted from Alice: {"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0x02", "A": "0xf60aca7dbe32c1bb2fa40f5056712d26df16cbdd09e02dee7443f0ade200adc38986756c8c6ad5ad22581d3b3e1ef83e1174208a1b49e01004d071e3a3f3753fd3f8be70ab0e77fc31054e1b2a1bcb4efae6b4ee7103a349d2a6f9d10ae68750fb3a5d0f1c779d3a92ed50674eed27eff8870a2c1e80432654b46f85bb2327ab9fa4ff66d150cde7f2292e616c6adc6adc402491e819ff3a7de6ff8a8bf51933cafd4446109f42c7e2ff298cdefc1a3beec299cf499b4a4aaba8995a255aa762"}
#Intercepted from Bob: {"B": "0x8d79b69390f639501d81bdce911ec9defb0e93d421c02958c8c8dd4e245e61ae861ef9d32aa85dfec628d4046c403199297d6e17f0c9555137b5e8555eb941e8dcfd2fe5e68eecffeb66c6b0de91eb8cf2fd0c0f3f47e0c89779276fa7138e138793020c6b8f834be20a16237900c108f23f872a5f693ca3f93c3fd5a853dfd69518eb4bab9ac2a004d3a11fb21307149e8f2e1d8e1d7c85d604aa0bee335eade60f191f74ee165cd4baa067b96385aa89cbc7722e7426522381fc94ebfa8ef0"}
#Intercepted from Alice: {"iv": "b46c8c3b24898940b85c17424b5ab358", "encrypted": "124ca6a920f35429cb2103df311dc8df0a1af42970724d146f7038dd1e01d2da"}
#Bob connects to you, send him some parameters: {"p": "0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff", "g": "0xf60aca7dbe32c1bb2fa40f5056712d26df16cbdd09e02dee7443f0ade200adc38986756c8c6ad5ad22581d3b3e1ef83e1174208a1b49e01004d071e3a3f3753fd3f8be70ab0e77fc31054e1b2a1bcb4efae6b4ee7103a349d2a6f9d10ae68750fb3a5d0f1c779d3a92ed50674eed27eff8870a2c1e80432654b46f85bb2327ab9fa4ff66d150cde7f2292e616c6adc6adc402491e819ff3a7de6ff8a8bf51933cafd4446109f42c7e2ff298cdefc1a3beec299cf499b4a4aaba8995a255aa762", "A":  "0x02"}          
#Bob says to you: {"B": "0x61ee12c53fc7df133a07ec80db8db961e975470dab2819aa8e52df66abf33370726cb033354711af8da20ed3510c176a644613a82012c542fc88567a2c4b7e7b393a003922c5a97a999cf333a4193231c1ba178cd34709e52c52f006d49adf584605d4ed7e8e1933bb7441b4861cfa0e496caa440cf811f9863c53f57be203c3089a786e7c7c2fa832071294008ad2e5f9c74c8bd60076f3c2e61fcf4691e9dfef3477eec85d5078f454899b61cfee964a9364cfc374ad1b6956fd0e91410921"}                                                                                
#Bob says to you: {"iv": "789a454684c29b67ef6f20e3bae01ce1", "encrypted": "4745c778660a905b2ab84cc0780c88d5de314df298420ea8eb4da9e67cd114f4c601affd81063cbdd3f50d2b915b3197a2926947fc8d1638b13c88e33198cd9321ff688cda12d160c5f271b9be263c23"}   


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


shared_secret = "0x61ee12c53fc7df133a07ec80db8db961e975470dab2819aa8e52df66abf33370726cb033354711af8da20ed3510c176a644613a82012c542fc88567a2c4b7e7b393a003922c5a97a999cf333a4193231c1ba178cd34709e52c52f006d49adf584605d4ed7e8e1933bb7441b4861cfa0e496caa440cf811f9863c53f57be203c3089a786e7c7c2fa832071294008ad2e5f9c74c8bd60076f3c2e61fcf4691e9dfef3477eec85d5078f454899b61cfee964a9364cfc374ad1b6956fd0e91410921"

iv = 'b46c8c3b24898940b85c17424b5ab358'
ciphertext = '124ca6a920f35429cb2103df311dc8df0a1af42970724d146f7038dd1e01d2da'
print ("Alice plain text:")
print(decrypt_flag(int(shared_secret, base=16), iv, ciphertext))


