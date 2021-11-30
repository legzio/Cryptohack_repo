
# The first I try some keys for ENCRYPT_FLAG(KEY). For KEY 00 00 00 00 00 00 00 00 ff ff ff ff ff ff ff ff  
# I received: {"ciphertext":"77f75fecda544ec75c75ac561e12411c6db41c858d5e9c3858b5dde4724ef30850dab6d4866bb9f7"}

# I used KEY and cipgertext to ENCRYPT(KEY, PLAINTEXT) where a PLAINTEXT I used ciphertext : 77f75fecda544ec75c75ac561e12411c6db41c858d5e9c3858b5dde4724ef30850dab6d4866bb9f7

# This back mi with: {"ciphertext":"63727970746f7b6e30745f346c6c5f6b3379735f3472335f673030645f6b3379737d060606060606"}

# I used this string to encode frlom HEX -> ASCII and I received:

# crypto{n0t_4ll_k3ys_4r3_g00d_k3ys}35f3472335f673030645f6b3379737d060606060606

