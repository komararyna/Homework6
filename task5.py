line = str(input('insert your phrase:'))
x = line.split(" ")
a = 0
for el in x:
    if len(el) > a:
        a = len(el)
        print(el)
    elif len(el) == a:
        print(el)
