# Design
j = 20
k = "- "

def design():
    print(f"{k}"*j, "\n")

list = ['a', 'b', 'z', 'd']
print("Main list", list)

list.pop()
print("Item poped:", list)

'''
list.clear()
print("list cleared:", list)
design()
'''

# learn index
if bool(list.count('c')) == True:
    print("After index:", list.index('c'))
else:
    pass
#reverse
list.reverse()
print("Reversed:", list)

#sort
list.sort()
print("After sorting:", list)

