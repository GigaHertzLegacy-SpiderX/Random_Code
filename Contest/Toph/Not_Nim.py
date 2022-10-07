n = int(input())

def pro(x=0, y=0, z=0):
    s1 = x - y
    if s1 <= z or z < ((x*z)/x):
        if i % 2 == 0:
            print("Alice")

        else:
            print("Bob")


for i in range(n):
    stick_j = int(input())
    stick_input = map(int, input().split())
    list_stick = list(stick_input)
    if sum(list_stick) != 2e+18 and stick_j != 100001:
        if len(list_stick) == stick_j:
            if stick_j == 3:
                pro(x=list_stick[0], y=list_stick[1], z=list_stick[2])
            elif stick_j == 2:
                pro(x=list_stick[0], y=list_stick[1])

            elif stick_j == 1:
                pro(x=[list_stick])

            else:
                pass

