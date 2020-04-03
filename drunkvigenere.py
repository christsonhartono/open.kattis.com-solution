enc = list(input())
key = list(input())

def dec(c, k, pos):
    if pos%2==0:
        if ord(c)>=ord(k):
            return chr(ord(c)-ord(k)+ord('A'))
        else:
            return chr(ord(c)-ord(k)+26+ord('A'))
    
    return chr((ord(c)+ord(k))%26+ord('A'))


print(''.join(list(map(dec,enc,key,range(len(enc))))))               
    
    
