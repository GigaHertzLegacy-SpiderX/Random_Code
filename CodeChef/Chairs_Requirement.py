# Coded by SpiderX

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    if (x-y) < 0:
        print(0)
    else:
        print(x-y)
