from sympy.ntheory.modular import crt

# Given the following set of linear congruences:
# x ≡ 2 mod 5
# x ≡ 3 mod 11
# x ≡ 5 mod 17 
#                       5*11*17 = 935
# Find the integer a such that x ≡ a mod 935

    
print(crt([5,11,17],[2,3,5]))
