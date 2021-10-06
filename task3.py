line = str(input('insert your phrase:'))
sum = 0
for el in line:
    count = int(str(ord(el))+" ")
    sum = sum + count
print(sum)
