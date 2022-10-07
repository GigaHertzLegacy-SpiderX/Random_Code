# Coded by SpiderX

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    week_days = x*7
    print(week_days-y)
