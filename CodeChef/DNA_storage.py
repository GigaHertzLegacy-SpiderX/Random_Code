# Coded by SpiderX

n = int(input())

for i in range(n):
    j = int(input())
    dna = input("")
    if len(dna) == j:
        # z = dna.replace("11", "G").replace("10", "C").replace("01", "T").replace("00", "A")
        x = 0
        y = 2
        emp = []
        for a in range(j):
            if dna[x:y] == "11" or "10" or "01" or "00":
                z = dna[x:y].replace("11", "G").replace("10", "C").replace("01", "T").replace("00", "A")
                emp.append(z)
                x += 2
                y += 2
                if len(emp) == j:
                    print(*emp, sep="")
