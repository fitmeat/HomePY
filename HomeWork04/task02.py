number = int(input('Введите количество кустов: '))
list = []

for i in range(number):
    list.append(int(input(f'Введите количесво ягод на {i+1} кусте: ')))
print(list)

max1 = list[0]
max2 = 0
max3 = 0
 
for i in range(1,len(list)):
    if list[i] > max1:
        max3 = max2
        max2 = max1
        max1 = list[i]
    elif list[i] > max2:
        max3 = max2
        max2 = list[i]
    elif list[i] > max3:
        max3 = list[i]
print(max1+max2+max3)
