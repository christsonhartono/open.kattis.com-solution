cipher = list(input())
key = list(input())
msg = list()
pos = 0

while(len(key)-3!=len(cipher)):
    mesage = ord(cipher[pos])-ord(key[pos])
    if(mesage<0):
        mesage+=26
    if(mesage>25):
        mesage-=26
    msg.append(chr(mesage+65))
    key.append(chr(mesage+65))
    pos+=1

print(''.join(msg))
