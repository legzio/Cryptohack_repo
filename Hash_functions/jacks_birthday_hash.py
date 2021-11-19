
#  JACK(secret) = 01011001101 -> 11 bits -> 2^11 -> 2048 keys
i = True
n = 1
while i==True:
    res = (2047/2048)**n
    
    if res > 0.5:
        print(" NOK", n, " , ",res)
    else: 
        print("OK", n, " , ",res)
        break
    n = n+1