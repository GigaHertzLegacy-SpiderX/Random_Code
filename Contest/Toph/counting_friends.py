# Coded by SpiderX360

len_arr = int(input())
list_arrA = []
list_arrB = []
list_all = []


for i in range(len_arr):
    a, b = map(int, input("").split())
    if a != b:
        list_arrA.append(a)
        list_arrB.append(b)
        # for all
        list_all.append(a)
        list_all.append(b)
    else:
        exit()


res = []
[res.append(x) for x in list_all if x not in res]
# 1 2
# 2 3
# 1 3
j = 0

for j in range(len_arr):
    print(list_all.count(res[j]))
