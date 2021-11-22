from sympy import primerange

# if [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237] are result of mod p it means that p must be bigger than the biggest one from lis - it means that p > 851 and has 3 digits:

primes = primerange(851,1000)
print(primes)

a = [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]


go = True
for p in primes:
    for x in range(2,1000):
        for i in range(len(a)-1):
            # left = (a[i]*x) %p
            # right = a[i+1]*x %p
            if (a[i]*x) % p == a[i+1]:
                go = True
                    # print("a =", a[i], "p =", p, "x =",x)
            else:
                go = False
                break
            # print(p,x)    
        if go:
            print(p," , ",x ) 
            break
    if go:
        break
print(p)

