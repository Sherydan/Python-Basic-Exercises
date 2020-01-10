from datetime import date
name = input('enter your name: ')
# puedo castear inmediatamente el input para que sea un int
age = int(input('enter your age: '))

def calc(age):
    year = date.today().year
    return (year + (100-age)) -1

year = calc(age)
print(f'you will turn 100yo in {year}')