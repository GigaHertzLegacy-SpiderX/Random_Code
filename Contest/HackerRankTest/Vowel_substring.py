x = input("").lower()
x_list = list(x)
y = int(input())

new = []

for i in range(len(x)):
    if x_list[i] == "a" or "e" or "i" or "o" or "u":
        try:
                z = x_list[i:i+y]
                new.append(z)
        except:
            pass
# print(new)
num_of_list = []

for k in range(len(new)):
    z = new[k].count('a') + new[k].count('e') + new[k].count('i') + new[k].count('o') + new[k].count('u')
    num_of_list.append(z)
    z = 0

z1 = max(num_of_list)
# print(z1)
z2 = num_of_list.index(z1)
print(*(new[z2]), sep="")


