n,r = list(map(int, input().split()))
bookedRoom = []

for i in range(r):
    room = int(input())
    bookedRoom.append(room)
    
if n==r:
    print("too late")
else:
    for i in range(1,n+1):
        if i not in bookedRoom:
            print(i)
            break
