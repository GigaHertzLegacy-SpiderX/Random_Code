# Coded by SpiderX

T = int(input())
total_list = []
for i in range(T):
    x, y = map(int, input().split())
    total = x*10 + y*90
    total_list.append(total)

for j in range(len(total_list)):
    print(total_list[j])
