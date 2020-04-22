def score(arr,n):
    result = 0

    for i in range(len(arr)):
        result+= arr[i]*((4/5)**i)

    return 1/5*result

def gscore(arr,n):
    result = 0
    
    for i in range(len(arr)):
        result+= score(arr[:i]+arr[i+1:], n-1)

    return result/n

n = int(input())
arr = []

for i in range(n):
    num = int(input())
    arr.append(num)

print(score(arr,n))
print(gscore(arr,n))
