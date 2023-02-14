a1 = int(input('Введите первый элемент арифмитической прогрессии: '))
n = int(input('Введите количество элементов: '))
d = int(input('Введите шаг: '))
list = []

for _ in range(n):
    list.append(a1+(n-1)*d)
    n = n-1
print(sorted(list))
