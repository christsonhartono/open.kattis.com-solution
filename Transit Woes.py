s,t,n = list(map(int, input().split()))
d = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
totalTime = 0

for i in range(n):
    totalTime+=d[i]
    if totalTime%c[i]==0:
        totalTime =(totalTime//c[i])*c[i]
    else:
        totalTime =((totalTime//c[i])+1)*c[i]
    totalTime+=b[i]

if (totalTime+d[-1])<=t:
    print("yes")
else:
    print("no")
