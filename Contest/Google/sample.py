n = int(input())
emp = []
if 1 <= n <= 100:
    for i in range(n):
        x, y = map(int, input().split())
        if 1 <= x <= 100000:
            candies = map(int, input().split())
            candies = list(candies)
            if len(candies) == x:
                divide = (sum(candies) % y)
                # print(f"Case #{n}:", divide)
                emp.append(divide)

for k in range(len(emp)):
    print(f"Case #{k+1}:", emp[k])
