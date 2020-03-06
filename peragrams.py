from string import ascii_lowercase 

lowercase = list(ascii_lowercase)
chars = {c : 0 for c in lowercase}
countOdd = 0

word = list(input())

for w in word:
    chars[w]+=1

for c in chars:
    if(chars[c]>0 and chars[c]%2==1):
        countOdd+=1

if countOdd == 0:
    print(0)
else:
    print(countOdd-1)
