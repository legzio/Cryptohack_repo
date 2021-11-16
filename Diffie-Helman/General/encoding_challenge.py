#!/usr/bin/env python3

from Crypto.Util.number import bytes_to_long, long_to_bytes
import base64
import codecs
import random
import telnetlib
import json



HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST, PORT)


def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

def decoder(type,text):
    # match x:
        # case "base64":
    if  type ==  "base64":  
        return base64.b64decode(text).decode()
        #case "hex":
    elif type == "hex":
        # out = bytes.fromhex(text).decode('utf-8')
        # print (out)
        # return out
        return bytes.fromhex(text).decode('utf-8')
        #case "rot13":
    elif type == "rot13":
        return codecs.decode(text,'rot13')
        #case "bigint":
    elif type == "bigint":
        return long_to_bytes(int(text, base=16)).decode()
        #case "utf-8":
    elif type == "utf-8":  
        res = ""
        for i in range(0,len(text)):
            res = res + chr(text[i]) 
            # print (res) 
        return res



# print(readline())
# print(readline())
# print(readline())
# print(readline())

for i in range(1,101):
    response = json_recv()
    #print(response)
    request = {"decoded": decoder(response["type"],response["encoded"])}
    #print(request)
    json_send(request)

response = json_recv()
print (response)    
