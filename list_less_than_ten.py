a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = []
for num in a:
    if num < 5:
        b.append(num)
print(b)

user_num = int(input('Give me a number: '))

for num in a:
    if num < user_num:
        c.append(num)
print(f'these numbers are smaller than your input {c}')