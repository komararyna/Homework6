line = str(input('insert your name:'))
if line[0].islower():
    print('name should start with big letter')
for el in range(1, len(line)):
    if line[el].isupper():
        print('other letters should be small')
        break
for i in line:
    if i.isalpha():
        continue
    print('name shouldn`t contain other symbols')
