from random import randint

coin = int(input('Введите количесво монет: '))
count = 0
eagle = 0
tails = 0
while count != coin:
    temp = randint(0,1)
    print(temp)
    if temp == 1:
        eagle += 1
    else:
        tails += 1
    count += 1
if eagle == 0 or tails == 0:
    print(f'Нужно перевернуть: {coin}')
elif eagle < tails:   
    print(f'Нужно перевернуть: {eagle}')
else:
    print(f'Нужно перевернуть: {tails}')
    