width = int(input())
n = int(input())
container = 0

for _ in range(n):
    w,l = list(map(int, input().split()))
    container = container + w*l

print(container//width)
