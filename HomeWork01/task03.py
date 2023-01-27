ticket = int(input('Введите номер билета: '))
first_part = ticket//1000
second_part = ticket%1000
sum_first = ((first_part//10 % 10) + first_part//100 + first_part % 10)
sum_second = ((second_part//10 % 10) + second_part//100 + second_part % 10)
if sum_first == sum_second:
    print('Ваш билет счастливый!')
else:
    print('Ваш билет обычный')

