# This task is very similar to our challange lab (encrypted image)
# Here we have the encrypted header of png file (challange lab has bmp). We know originate png file header:

# follow https://parsiya.net/blog/2018-02-25-extracting-png-chunks-with-go/ png header:

# header_png = bytes([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a, 0x00, 0x00, 0x00, 0x0d, 0x49, 0x48, 0x44, 0x52])

# encrypted file (I couldn't paste here):

import requests

header_png = bytes([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a, 0x00, 0x00, 0x00, 0x0d, 0x49, 0x48, 0x44, 0x52])

def read_enc():
    encrypted = requests.get('http://aes.cryptohack.org/bean_counter/encrypt/')
    return encrypted.json()['encrypted']


enc_png_file = bytes.fromhex(read_enc())

# print (bytes.fromhex(enc_png_file))
# print(enc_png_file)

# because we don't need decode png file in 100%, we need only be able to read flag, so I assign, that x value will be the same for all blocks.

x = []
for i in range(16):
    x.append(enc_png_file[i] ^ header_png[i])

final_png_file = [0]*len(enc_png_file)
# for i in range(len(enc_png_file)):
    # final_png_file[i] = 0

for i in range(len(enc_png_file)):
    final_png_file[i] = x[i % 16] ^ enc_png_file[i]

with open('decoded_file.png', 'wb') as file:
    file.write(bytes(final_png_file))   



