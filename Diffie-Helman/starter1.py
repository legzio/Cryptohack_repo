p=991
g=209

d=pow(g,-1,p)

print(d)

# mozna tez tak zrobic (brute force):
# for i in range(p)
#   if ((g*i) % p) ==1
#       print (i)
