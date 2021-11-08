
from sympy.ntheory import factor_
from sympy.ntheory.generate import prime

N = 510143758735509025530880200653196460532653147
#sqrt_N = int(math.sqrt(N))
#print(sqrt_N)

print(factor_.primefactors(N))

# result was: [19704762736204164635843, 25889363174021185185929]
