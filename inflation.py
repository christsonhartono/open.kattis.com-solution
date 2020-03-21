n = int(input())

canisters = list(map(int, input().split()))
canisters.sort()

cond = 1
f = 1

for balon in range(n,0,-1):
    tst = balon - canisters[balon-1]
    if tst>=0:
        candidate = canisters[balon-1]/balon
        if candidate <= f:
            f = candidate
    elif tst<0:
        cond = 0

if cond==1:
    print(f)
else:
    print('impossible')
