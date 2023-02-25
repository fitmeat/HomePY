class Model:
    
    phone_book = []
    path = 'phone_book_oop/phone_book.txt'

    def __init__(self, path):
        self.path = path
        with open(path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
            for contact in data:
                new = contact.strip().split(';')
                new_dict = {}
                new_dict['name'] = new[0]
                new_dict['phone'] = new[1]
                new_dict['comment'] = new[2]
                self.phone_book.append(new_dict)

    def get(self):
        return self.phone_book

    def add(self, new_dict: dict):
        self.phone_book.append(new_dict)

    def save_file(self):
        data = []
        for contact in self.phone_book:
            data.append(';'.join(contact.values()))
        data = '\n'.join(data)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)

    def find(self, find_option: str):
        all_find = []
        for contact in self.phone_book:
            for element in contact.values():
                if find_option.lower() in element.lower():
                    all_find.append(contact)
        return all_find

    def change_contact(self, ind: int, contact: dict):
        self.phone_book.pop(ind-1)
        self.phone_book.insert(ind-1, contact)

    def delete(self, ind: int):
        self.phone_book.pop(ind-1)

    def get_name(self, ind: int):
        return self.phone_book[ind-1].get('name')
