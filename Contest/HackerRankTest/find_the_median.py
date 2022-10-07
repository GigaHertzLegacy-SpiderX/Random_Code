
n = int(input())
usr = input("").split()
usr_list = sorted(list(usr))

if n % 2 != 0 and len(usr_list) == n:
        print(usr_list[((n+1) // 2)])

else:
    exit()