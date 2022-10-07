# Coded by SpiderX

n = int(input())
total1 = []
t2 = []

for i in range(1, n+1):
    if n % i == 0:
        total1.append(i)

# [1, 2, 5, 10]
for j in range(len(total1)):
    if total1[j] > 2:
        # print('total1 J', total1[j])
        t2.append(j)
        j +=1

t2 = list(dict.fromkeys(t2))

if len(t2) > 2:
    print("Never give up")

else:
    print("Well done")
