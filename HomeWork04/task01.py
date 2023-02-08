n = int(input('Введите количесво элементов первого множества: '))
m = int(input('Введите количесво элементов второго множества: '))

list1 = []
list2 = []

for i in range(n):
    list1.append(input('Введите число: '))
print(f'Первое множество: {list1}')

for i in range(m):
    list2.append(input('Введите число:'))
print(f'Второе множество: {list2}')

my_set1 = set(list1)
my_set2 = set(list2)

result_set = my_set1.intersection(my_set2)
print(sorted(result_set))

