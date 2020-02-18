cipher = list(input())
key = list(input())
keyLength = len(key)
msg = list()
pos = 0

while(len(key)-keyLength!=len(cipher)):
    message = ord(cipher[pos])-ord(key[pos])
    if(message<0):
        message+=26
    if(message>25):
        message-=26
    msg.append(chr(message+65))
    key.append(chr(message+65))
    pos+=1

print(''.join(msg))
