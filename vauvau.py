a,b,c,d = list(map(int, input().split()))
heroes = list(map(int,input().split()))

for hero in heroes:
    count = 0
    n = hero//(a+b)

    if hero >= (a+b)*n+1 and hero <= (a+b)*n+a:
        count+=1

    n = hero//(c+d)

    if hero >= (c+d)*n+1 and hero <= (c+d)*n+c:
        count+=1

    if count==1:
        print("one")
    elif count==2:
        print("both")
    else:
        print("none")
