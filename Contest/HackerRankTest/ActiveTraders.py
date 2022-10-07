n = int(input())
customers = []
for i in range(n):
    usr = input("")
    customers.append(usr)

unique_customers = set(customers)
unique_customers = list(sorted(unique_customers))

for i in range(len(unique_customers)):
    countOF = customers.count(unique_customers[i])
    parcent = (countOF / n) * 100
    if parcent >= 5:
        print(unique_customers[i])


