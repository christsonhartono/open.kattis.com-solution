def bus(n):
    passenger = 0
    while(n>0):
        passenger+= .5
        passenger*=2
        n-=1;
    return int(passenger)
    
t = int(input())
for i in range(t):
    n = int(input())
    print(bus(n))
