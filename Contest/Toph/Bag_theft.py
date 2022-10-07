# Coded by SpiderX

l = int(input())

for i in range(l):
    t = input("")
    t_list = list(t)

    k1 = int(''.join(t_list[:2]))
    # print(k1) #09
    k2 = int(''.join(t_list[2:]))
    # print(k2) #30

    # Reduce
    m_time = k2 // 15
    m_time2out = 8 * m_time

    # In Hours
    h_time = (k1 - 9)
    # print(h_time)
    h_time2 = 64 * (h_time)
    # hourly in

    # 5 min in
    m2_time = k2 // 5
    m2_timein = 8 * m2_time

    TOTAL = h_time2 - m_time2out + m2_timein
    print(TOTAL)

