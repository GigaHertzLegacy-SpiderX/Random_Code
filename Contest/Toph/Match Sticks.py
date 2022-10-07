
def num(n):
    if n % 5 == 0:
        print("Yes")
    else:
        print("No")

for i in range(2):
    n = int(input())
    if 4 < n < 100000:
        num(n)
