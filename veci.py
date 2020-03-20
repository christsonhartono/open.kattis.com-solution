n = list(input())

start = int(''.join(n))+1

if n == sorted(n, reverse=True):
    print(0)
else:
    cond = 0
    while cond==0:
        if sorted(list(str(start))) == sorted(n):
            print(start)
            cond = 1
        else:
            start+=1
