from random import randint as rd

length = int(input('Введите длину списка: '))
list = []

for _ in range(length):
    list.append(rd(1,100))
print(list)

number = int(input('Ввидите искомое число: '))
count = 0
found = list[0]

for item in list:
    if item == number:
        count += 1
    elif abs(item - number) < abs(found - number):
        found = item

if count != 0:
    print(f'Искомое число втречается {count} раз(а)')
else:
    print(f'Самое близкое число к искомому: {found}')