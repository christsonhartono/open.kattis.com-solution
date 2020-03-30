n = int(input())
count = 0

for i in range(n):
    label = input().lower()
    if 'pink' in label or 'rose' in label:
        count+=1

if count>0:
    print(count)
else:
    print('I must watch Star Wars with my daughter')
