number = int(input('Enter a number: '))

if (number % 4) == 0:
    print(f'{number} is multiple of 4')
elif (number % 2) == 0:
    print(f'{number} is even')
else:
    print(f'{number} is odd')

# if (number % 2) == 0:
#     print(f'{number} is even')
# else:
#     print(f'{number} is odd')