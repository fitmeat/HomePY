from random import randint as rd

low = int(input('Введите нижнюю границу диапазона: '))
hight = int(input('Введите верхнюю границу диапазона: '))
n = int(input('Введите количество элементов списка: '))
list = []
res_list = []

for _ in range(n):
    list.append(rd(-10,10))
print(list)

for i in range(len(list)):
    if list[i] >= low and list[i] <= hight:
        res_list.append(i)
print(res_list)