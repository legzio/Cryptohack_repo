
#  my plain text = aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa     - 3 blocks x 16bytes
#  my plain text in HEX = 616161616161616161616161616161616161616161616161616161616161616161616161616161616161616161616161
#  my cipher = 9ccd4ea6c9454bd7ee813073e40a508d851a4d5696d2f494f58c5744e67d58d4e6f8e64b3ccb99bc1354355c11e666ed

# Form code:  
# cipher = AES.new(KEY, AES.MODE_CBC, KEY)  --> KEY = iv

from typing_extensions import IntVar


p1 - first block, p2 - second block, p3 - third BlockingIOError

p1 = c1 ^ key ^ iv
p2 = c2 ^ key ^ c1
p3 = c3 ^ key ^ c2

# Let assign c2 = 00000000000000000000000000000000, and c3 = c1 and modify ciphertext in that 
#  Then :
p2 = 0 ^ key ^ c1 --> p2 = key ^ c1
p3 = c1 ^ key ^ 0 --> p3 = key ^ c1 --> c1 = p3 ^ key
p1 = key ^ c1 ^ iv --> c1 = p1 ^ key ^ iv

p1 ^ key ^ iv = p3 ^ key --> p1 ^ p3 = key ^ key ^ iv (key^key=0) --> iv = p1 ^ p3

#  if I modify ciphertext I can use receive(ciphertext) function, which in error giving back decrypted plaintext:

    #    return {"error": "Invalid plaintext: " + decrypted.hex()}

c1 = 9ccd4ea6c9454bd7ee813073e40a508d
c2 = 851a4d5696d2f494f58c5744e67d58d4
c3 = e6f8e64b3ccb99bc1354355c11e666ed
c2' = 00000000000000000000000000000000

My new ciphertext = c1 + c2' + c1 = 9ccd4ea6c9454bd7ee813073e40a508d000000000000000000000000000000009ccd4ea6c9454bd7ee813073e40a508d

I received error:

{"error":"Invalid plaintext: 61616161616161616161616161616161ce7462ef6534d203f82e9eec3bb4c0e52c523479b89a874f21e99159172983fa"}

So now my new p3 = 2c523479b89a874f21e99159172983fa

iv = p1 ^ p3 = 61616161616161616161616161616161 ^ 2c523479b89a874f21e99159172983fa = 4d335518d9fbe62e4088f0387648e29b

AND finally iv = KEY so I use get_flag(key):

{"plaintext":"63727970746f7b35306d335f703330706c335f64306e375f3768316e6b5f49565f31355f316d70307237346e375f3f7d"}

decoded from HEX:

crypto{50m3_p30pl3_d0n7_7h1nk_IV_15_1mp0r74n7_?}