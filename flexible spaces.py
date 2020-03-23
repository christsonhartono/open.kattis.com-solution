w, p = list(map(int, input().split()))
inp = list(map(int, input().split()))

spaces = [0]+inp+[w]

result = []

for i in range(1,len(spaces)):
    for j in range(i):
        result.append(spaces[i]-spaces[j])

print(*set(sorted(result)))
