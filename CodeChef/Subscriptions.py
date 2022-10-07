# Coded by SpiderX

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    if x % 6 == 0:
        z = x // 6
        print(y*z)

    else:
        z1 = (x // 6) + 1
        print(z1*y)
