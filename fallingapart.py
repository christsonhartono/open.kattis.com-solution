n = int(input())

alice, bob = (0,0)

arr = list(map(int, input().split()))

for i in range(n):
    if(i%2==0):
        alice+=arr.pop(
                arr.index(max(arr)))
    else:
        bob+=arr.pop(
                arr.index(max(arr)))

print(alice, bob)
