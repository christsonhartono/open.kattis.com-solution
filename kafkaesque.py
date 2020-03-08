n = int(input())
countPass = 0
prev = None

for i in range(n):
    c = int(input())
    if i==0 or c < prev: 
        countPass+=1
    prev = c

print(countPass)
        
    
