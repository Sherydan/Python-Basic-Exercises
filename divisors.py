num = int(input('Give me a number: '))
div = []

# desde pyton 3 "range" es un iterator, por lo tanto se debe castear a list antes
x = list(range(1, num+1))

for number in x:
    if (num % number) == 0:
        div.append(number)

print(div)
