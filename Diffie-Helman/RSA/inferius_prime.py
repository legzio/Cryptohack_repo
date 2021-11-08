#!/usr/bin/env python3

from sympy.ntheory import factor_

from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD

e = 3
n = 742449129124467073921545687640895127535705902454369756401331
print(n)

ct = 39207274348578481322317340648475596807303160111338236677373


# values p and q received from factordb.com 


p = 752708788837165590355094155871
q = 986369682585281993933185289261

print(p * q)

phi = (p - 1) * (q - 1)
d = inverse(e, phi)



print(f"n = {n}")
print(f"e = {e}")
print(f"ct = {ct}")

pt = pow(ct, d, n)
decrypted = long_to_bytes(pt)
print(decrypted)
