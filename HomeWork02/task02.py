from random import randint as rd

number1 = rd(1,10)
number2 = rd(1,10)
print(f'Сумма загаданных чисел: {number1 + number2}')
print(f'Произведение загаданных чисел: {number1 * number2}')

while True:
    
    result1 = int(input('Первое число: '))
    result2 = int(input('Второе число: '))
    
    if result1 == number1 and result2 == number2:
        print(f'Поздравляем! Ты угадал, это числа {result1} и {result2}')
        break
    elif result1 == number2 and result2 == number1:
        print(f'Поздравляем! Ты угадал, это числа {result1} и {result2}')
        break
    else: 
        print('Пробуй еще раз!')