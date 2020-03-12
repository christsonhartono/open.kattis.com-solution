p,q,s = list(map(int, input().split()))

if(max([p,q])%min([p,q])==0 and max([p,q])<=s):
    print("yes")
else:
    bigval = max([p,q])
    lowval = min([p,q])
    loop=1
    cond=0
    while(bigval*loop<=s):
       test = bigval*loop
       if(test%lowval==0):
           cond = 1
           break
       loop+=1
        
    print("yes" if cond==1 else "no")
