a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# set no acepta duplicados 
c = set()

for num in a:
    if num in b:
        c.add(num)

print(c)



