from sympy.core.numbers import igcd

p = 26513 
q = 32321

# p * u + q * v = gcd(p,q) --> u = (gcd(p,q) - q*v)/p

gcd = igcd(p,q)

for v in range (-q,q):
    for u in range (-p,p):
        if p * u + q * v == gcd:
            print ("u = ", u)
            print ("v = ",v)
            # print("crypto{", u, ",",v,"}")
            break

print("KONIEC")