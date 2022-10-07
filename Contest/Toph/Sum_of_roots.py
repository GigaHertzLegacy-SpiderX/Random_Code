# Coded by SpiderX

a, b, c = map(int, input().split())

x = a**(1/2)
y = b**(1/2)
z = c**(1/2)

res = x + y + z
print(res.__floor__())

# # Coded by SpiderX
#
# list1 = list(map(int, input().split()))
#
# res = 0
# for i in range(len(list1)):
#     res += list1[i]**(1/2)
#
# print(res)

