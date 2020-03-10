n = int(input())

rectangles = list()
circles = list()

for _ in range(n):
    inp = input().split()
    if inp[0]=='circle':
        circles.append(list(map(int, inp[1:])))
    else:
        rectangles.append(list(map(int, inp[1:])))

t = int(input())

for _ in range(t):
    target = 0
    x,y = list(map(int, input().split()))
    
    for x1,y1,x2,y2 in rectangles:
        if(x >= x1
           and x <= x2
           and y >= y1
           and y <= y2):
            target+=1

    for x1,y1,r in circles:
        if(((x-x1)**2+(y-y1)**2) <= r**2):
            target+=1

    print(target)
