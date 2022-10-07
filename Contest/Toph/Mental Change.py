# Coded by SpiderX

n = int(input())

emp = []
for i in range(n):
    x = int(input())
    emp.append(x)

for j in range(0, len(emp)):
    if j == 0:
        print(1, end=" ")
    else:
        if emp[j] > emp[j-1]:
            print(2, end=" ")
        else:
            print(1, end=" ")


