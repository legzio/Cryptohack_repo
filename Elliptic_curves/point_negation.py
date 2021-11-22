from math import sqrt

# E: Y2 = X3 + 497 X + 1768, p: 9739 
# Using the above curve, and the point P(8045,6936), find the point Q(x,y) such that P + Q = O.

# if P+Q = 0 then Q = -P --> -P = (8045,-6936) --> yq = -6936 mod p

x = 8045
p = 9739
yq = -6936 % p
print("crypto{",x,",",yq,"}")
