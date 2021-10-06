line = str(input('insert your phrase:'))
x = line[0]
lin = line[1:]
for el in lin:
    if el == x:
        break
b = el
li = lin.find(b)
print('Вовочка писал:', line[0:li+1])