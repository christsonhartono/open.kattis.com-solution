from collections import defaultdict

try:
    listNumber = 1

    while True:
        n = int(input())
        
        if n==0:
            break

        animals = defaultdict(int)
        
        for _ in range(n):
            animal = input().split()
            animals[animal[-1].lower()]+=1

        print("List {}:".format(listNumber))

        for key, val in sorted(list(zip(animals.keys(), animals.values()))):
            print('{} | {}'.format(key,val))

        listNumber+=1
except:
    pass
            
