n = int(input())

max = None
arr = [0]*100000

for i in range(n):
    idx = int(input())
    arr[idx]=1
    if(i==n-1):
        max = idx

cond = 1

for i in list(range(1,max+1)):
    if(arr[i]==0):
        print(i)
        cond = 0

if cond==1:
    print('good job')
