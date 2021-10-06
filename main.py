str = str(input('insert your phrase:'))
count = 0
for el in str:
    if el == 'b':
        count += 1
print(count)