import numpy as np

pos = int(input())
step = [pos]

branch = np.zeros((101,101), int)

while True:
    inp = list(map(int, input().split(' ')))
    if inp[0]== -1:
        break
    for i in inp[1:]:
        branch[i][inp[0]] = 1 
    
cond = 1

while cond!=0:
    for i in range(len(branch[pos])):
        if branch[pos][i]==1:
            pos = i
            step.append(i)
            break
        elif i==len(branch[pos])-1:
            cond=0
            break

for i in step:
    print(i, end=" ")

    
