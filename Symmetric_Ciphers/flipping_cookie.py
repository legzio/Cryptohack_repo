


# Get cookie interact page give:
# {"cookie":"a9073c94f730c5e00dfe6fc704c9edcfa90728f0914ebb50b41e2c1dcc708cd8c779cdf7f8df3e0a705358dc983707ee"}

# From code we see that iv is first 16 bytes of cookie string.
iv = a9073c94f730c5e00dfe6fc704c9edcf


# after CHECK_ADMIN function we receive:

# {"error":"Only admin can read the flag"}

# it means that there is necessary to set 'admin=True' in request CHECK_ADMIN function.

# the admin=False is encrypted in cookie as first 16bytes, so it must be decrypted and replace with admin=True

# 
CBC mode descirbe:

plaintext ^ iv ^ cipher = Key

In this ccokie we know that first 16 bytes is 'admin=False;expi' (reader from attaches het_cookie() function)

old_plain = admin=False;expi = HEX (61646d696e3d46616c73653b65787069)
new_plain = ;admin=True;expi = HEX (3b61646d696e3d547275653b65787069)  - extended with ';' to 16bytes

key = old_plain ^ iv  --> old_plain = key ^ iv
key = new_plain ^ iv' --> iv' = new_plain ^ key
iv' = old_plain ^ iv ^ new_plain

iv' = 61646d696e3d46616c73653b65787069 ^ 3b61646d696e3d547275653b65787069 ^ a9073c94f730c5e00dfe6fc704c9edcf = f3023590f063bed513f86fc704c9edcf

cookie = f3023590f063bed513f86fc704c9edcfa90728f0914ebb50b41e2c1dcc708cd8c779cdf7f8df3e0a705358dc983707ee
iv = a9073c94f730c5e00dfe6fc704c9edcf

OUTPUT:

{"flag":"crypto{4u7h3n71c4710n_15_3553n714l}"}