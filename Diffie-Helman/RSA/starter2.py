# N = p * q
e = 65537
p = 17
q = 23
m = 12

# ciphertext = m^e mod N

N = p * q

print (pow(m,e,N))
