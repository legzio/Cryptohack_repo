p=28151
for x in range(1,p):
    g1 = x
    ind = 1
    g2 = g1 % p
    while (g2 != 1):
        g2 = (g2 * g1) % p
        ind = ind +1
    if (ind==(p-1)):
        print (g1)
        break