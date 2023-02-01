N = int(input('Введите число N: '))
k = 0
list = []
while True:
    result = 2 ** k
    k += 1
    if result > N:
        break
    print (result)