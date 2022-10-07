# Coded by SpiderX

n, q = map(int, input().split())

b_l_r = []  # bothI+J

for z in range(q):
    if n or q <= 1000 and n or q >= 1:
        l, r = map(int, input().split())
        if l and r <= 1000 and l and r >= 1:
            l_list = []  # i
            r_list = []  # j

            for i in range(1, l+1):
                if l % i == 0:
                    l_list.append(i)

            for j in range(1, r+1):
                if r % j == 0:
                    r_list.append(j)

            for k in l_list and r_list:
                if k not in b_l_r:
                    b_l_r.append(k)
                    set(b_l_r)
                    if len(b_l_r) > 1:
                        if b_l_r[0] == 1:
                            b_l_r.remove(1)

            if not b_l_r:
                b_l_r.append(1)

            print(*b_l_r)
