from math import factorial

#  JACK(secret) = 01011001101 -> 11 bits -> 2^11 -> 2048 keys
#  p = 2048!/(2048^2*(2048-2)!)

i = True
n = 1
while i==True:
    res = 1 - (factorial(2048)/((2048**n)*factorial(2048-n)))
    # res = ((1/2048) * (2/2048))**n
    
    if res < 0.75:
        print(" NOK", n, " , ",res)
    else: 
        print("OK", n, " , ",res)
        break
    n = n+1
