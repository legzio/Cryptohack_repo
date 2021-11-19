from sympy import sqrt_mod

# a^2 = x mod p

p = 29
ints = [14, 6, 11] 

for i in ints:
    a = sqrt_mod(i,p,all_roots=True)
    print (a)


