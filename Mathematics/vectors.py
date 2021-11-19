from numpy.core.defchararray import multiply
from sympy.physics.vector import ReferenceFrame
from numpy import *

# Time for the flag! Given a three dimensional vector space defined over the reals, where v = (2,6,3), w = (1,0,0) and u = (7,7,2), calculate 3*(2*v - w) ∙ 2*u.

v = ReferenceFrame("V")
w = ReferenceFrame("W")
u = ReferenceFrame("U")
v = [2,6,3]
w = [1,0,0]
u = [7,7,2]
# res = 2*v
res = multiply(2,v)
print(res)
# (2*v - w)
res = add(res,negative(w))
print(res)
# 3*(2*v - w)
res = multiply(3,res)
print(res)
# 2*u
u2 = multiply(2,u)
# 3*(2*v - w) ∙ 2*u
res = vdot(res,u2)
print(res)