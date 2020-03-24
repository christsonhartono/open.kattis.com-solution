p,t = list(map(int, input().split()))
count = 0

for _ in range(p):
    sum = 0
    for i in range(t):
        s = input()
        if s.islower():
            sum+=1
        else:
            test = list(s)
            test[0] = test[0].lower()
            if(''.join(test).islower()):
                sum+=1
    if sum==t:
        count+=1

print(count)
