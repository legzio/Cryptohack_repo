

{"ciphertext":"b9045aa72fad71343dec83c0c9d3047832142c8656d2f1ed7da8679ab958e19b1bcd14671bacf0bca609b50f04d45a6c"}

encrypted with CBC
iv = b9045aa72fad71343dec83c0c9d30478

decrypt(ciphertext) used ciphertext without iv part:

32142c8656d2f1ed7da8679ab958e19b1bcd14671bacf0bca609b50f04d45a6c

in response:

{"plaintext":"da7623d75bc20a075e8edcf5bcb06f4d6d205ab667b6aedc4af746bb9879c0e6"}

Now this plain xor with iv will give the first 16butes of flag:

da7623d75bc20a075e8edcf5bcb06f4d ^ b9045aa72fad71343dec83c0c9d30478

crypto{3cb_5uck5

Next second part of plain xor with first part of ciphertext:

6d205ab667b6aedc4af746bb9879c0e6 ^ 32142c8656d2f1ed7da8679ab958e19b

_4v01d_17_!!!!!}


so FLAG = crypto{3cb_5uck5_4v01d_17_!!!!!}