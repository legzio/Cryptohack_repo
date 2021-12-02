Encode_falg() execute:

{"ciphertext":"3e8ee6320342308af700d646dc2058f0269a747b6347b11be0a32d9ed7efb8ce29ca1234d2d0dcb35d98e541fb4f3f3c23"}

iv = 3e8ee6320342308af700d646dc2058f0
rest = 269a747b6347b11be0a32d9ed7efb8ce29ca1234d2d0dcb35d98e541fb4f3f3c23 - 33bytes, means 2 x 16 +1byte

ENCRYPT(plain,iv)

I choose my plain text and use iv from flag encryption:

plain = '11111111111111110000000000000000' -> hex:  3131313131313131313131313131313130303030303030303030303030303030

iv = 3e8ee6320342308af700d646dc2058f0

Using ENCRYPT(plain, iv):

{"ciphertext":"74d93c3a2619fb1ab7f0439ed381bc867497113390d18fb701f7f450ea4e3e2d"}

Let's divide these information in 16bytes blocks.
plain = 3131313131313131313131313131313130303030303030303030303030303030
p0 = 31313131313131313131313131313131
p1 = 30303030303030303030303030303030

my_ciphertext = 74d93c3a2619fb1ab7f0439ed381bc867497113390d18fb701f7f450ea4e3e2d
cm0 = 74d93c3a2619fb1ab7f0439ed381bc86
cm1 = 7497113390d18fb701f7f450ea4e3e2d

plain_flag = ???
pf0 = ??
pf1 = ??

cipher_flag = 269a747b6347b11be0a32d9ed7efb8ce29ca1234d2d0dcb35d98e541fb4f3f3c23
c0 = 269a747b6347b11be0a32d9ed7efb8ce
c1 = 29ca1234d2d0dcb35d98e541fb4f3f3c
1 byte = 23

From OFB mode encryption diagram we see, if for both encryption I use the same iv then:

p0 ^ x0 = cm0
p1 ^ x1 = cm1

pf0 ^ x0 = c0
pf1 ^ x1 = c1

from these:

pf0 = c0 ^ cm0 ^ p0 = 269a747b6347b11be0a32d9ed7efb8ce ^ 74d93c3a2619fb1ab7f0439ed381bc86 ^ 31313131313131313131313131313131 = 63727970746f7b3066625f31355f3579 -> ascii -> crypto{0fb_15_5y
pf1 = c1 ^ cm1 ^ p1 = 29ca1234d2d0dcb35d98e541fb4f3f3c ^ 7497113390d18fb701f7f450ea4e3e2d ^ 30303030303030303030303030303030 = 6d6d3337723163346c5f212121313121 -> ascii -> mm37r1c4l_!!!11!

one byte was left, but after decode flag I can assign, that last char is "}"
so the flag = crypto{0fb_15_5ymm37r1c4l_!!!11!}
