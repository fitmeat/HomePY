list_vow = ['а', 'о', 'у', 'ы', 'э', 'е', 'ё', 'и', 'ю', 'я']
stirng = input('Введите стихотворение: ')
number_of_frase= list(enumerate(stirng.split()))
print(f'Количество фраз: {len(number_of_frase)}')
list_text = stirng.split('-')
count = 0

for item in list_text:
        number = list(enumerate(item))
        for i in number:
            if i[1] in list_vow:
                count += 1
print(f'Количество гласных: {count}')

if count % len(number_of_frase) == 0:
    print('Парам пам-пам')
else:
    print('Пам парам')
