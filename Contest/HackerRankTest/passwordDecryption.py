# Coded by SpiderX

n = input("")
n_list = list(n)
new = []

for i in range(len(n_list)):
    if n_list[i] == "*":
        pass

    elif str(n_list[i]).islower() and str(n_list[i+1]).isupper():
        n_list[i], n_list[i+1] = n_list[i+1], n_list[i]
        n_list.insert((i+2), "*")

    elif str(n_list[i]).isnumeric():
        # n_list.insert(0, n_list[i])
        new.insert(0, n_list[i])
        n_list[i] = str(0)

    else:
        pass


print(*new, *n_list, sep="")

