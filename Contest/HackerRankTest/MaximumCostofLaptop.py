n = int(input())
n1_list = []
for i in range(n):
    n1 = int(input())
    n1_list.append(n1)

if len(n1_list) == n:
    n3 = int(input())
    n2_list = []
    for i2 in range(n3):
        n2 = input("")
        n2_list.append(n2)

    if len(n2_list) == n3:
        DailyCount = int(input())
        list_of_cost = []
        cost = 0
        legal = 0

        for k in range(len(n2_list)):
            if legal == DailyCount:
                list_of_cost.append(cost)
                legal = 0
                cost = 0

            elif n2_list[k] == "legal":
                legal += 1
                cost += int(n1_list[k])

            elif n2_list[k] == "illegal":
                cost += int(n1_list[k])

            else:
                k += 1

        try:
            print(max(list_of_cost))

        except:
            print(0)
