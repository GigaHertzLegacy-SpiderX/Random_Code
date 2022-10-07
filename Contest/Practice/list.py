# automate tools
j = 18 #distance of row
k = "-  " #design of row

print(f"{k}"*j)
list = ['a', 'b', 'c', 'd']
print('printed list:', list)
print(f"{k}"*j)
list.append('x')
print('appended list:', list)
print(f"{k}"*j)
list.extend('y')
print('extended list:', list)
print(f"{k}"*j)
list.insert(3, 'z')
print('inserted list:', list)
print(f"{k}"*j)
if bool(list.count('x')) == True:
    list.remove('x')
    print('item removed:', list)
else:
    print("Value Error!")
print(f"{k}"*j)
