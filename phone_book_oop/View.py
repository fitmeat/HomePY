class View:
    
    def menu():
        print('''\nГлавное меню
        1. Открыть файл
        2. Сохранить файл
        3. Показать контакты
        4. Добавить контакт
        5. Изменить контакт
        6. Найти контакт
        7. Удалить контакт
        8. Выход''')
        while True:
            try:
                button = int(input('Выберите действие: '))
                if 0<button<9:
                    return button
                else:
                    print('Введите число от 1 до 8')
            except:
                print('Вводи цифры!')

    def show_contact(self, pb: list[dict]):
        if pb == []:
            print('Телефонная книга пуста или файл не открыт')
        else:
            for i, contact in enumerate(pb, 1):
                self.name = contact.get('name')
                self.phone = contact.get('phone')
                self.comment = contact.get('comment')
                print(f'{i}. {self.name:<20} {self.phone:<15} {self.comment:<20}')

    def input_new_contact(self):
        self.name = input('Введите имя и фамилию: ')
        self.phone = input('Введите номер телефона: ')
        self.comment = input('Введите комментарий: ')
        new = {'name': self.name, 'phone': self.phone, 'comment': self.comment}
        return new

    def find_contact(self):
        find = input('Введите искомый элемент: ')
        return find

    def get_ind(self):
        ind = int(input('Введите индекс: '))
        return ind

    def confirm(self, condition: str, name: str):
        answer = input(f'Вы действительно хотите {condition} контакт {name}? (y/n)')
        if answer == 'y':
            return True
        else:
            return False

    def confirm_changes(self):
        answer = input('У вас есть несохраненные изменения, хотите их сохранить? (y/n)')
        return True if answer == 'y' else False