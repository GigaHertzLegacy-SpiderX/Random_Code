# Coded by SpiderX

n = int(input())
input = list(map(int, input().split()))
for i in range(n):
    if input[i] % 2 == 0:
        print(0, end=" ")
    else:
        print(1, end=" ")