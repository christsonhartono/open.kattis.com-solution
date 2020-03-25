n = int(input())

for i in range(n):
    r,p,d = list(map(int,input().split()))

    totalWeight = 0
    ingridient = dict()
    scaling = d/p
    
    for j in range(r):
        q = input().split(' ')
        ingridient[q[0]] = float(q[-1])
        if float(q[-1])==100:
            totalWeight = float(q[-2])

    totalWeight*=scaling
    
    print("Recipe #",i+1)
    for k in ingridient.keys():
        print(k, ingridient[k]*totalWeight/100)
    print('-'*40)
