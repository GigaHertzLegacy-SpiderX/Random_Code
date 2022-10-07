old_string = "ababa"
new_string = "aba"

ways = 0
while_counts = 0

while True:
    znew = sorted(list(new_string))
    zolD = list(old_string)

    count_new = old_string
