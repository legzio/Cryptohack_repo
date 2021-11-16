from Crypto.Util.number import long_to_bytes

key1 = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf 
key12 = 0x37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
key23 = 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
key123f = 0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf 

key2 = key12 ^ key1
key3 = key23 ^ key2
flag = key123f ^ key1 ^ key2 ^ key3
print(long_to_bytes(flag))


