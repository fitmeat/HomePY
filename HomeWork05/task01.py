def degree(a,b):
    result = 1
    if b == 0:
        return 1
    result *= a
    return degree(a,b-1) * result

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
print(f'a^b = {degree(a,b)}')