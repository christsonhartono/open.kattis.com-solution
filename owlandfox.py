n = int(input())

for _ in range(n):
    num = list(input())
    for i in range(len(num)-1,-1,-1):
        if int(num[i])>0:
            num[i] = str(int(num[i])-1)
            break
    print(int(''.join(num)))
    
