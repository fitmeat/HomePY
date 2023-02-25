from View import View
from Model import Model

def start():
    pb = Model('phone_book_oop/phone_book.txt')
    vi = View()
    while True:
        button = View.menu()
        match button:
            case 1:
                pb.__init__('phone_book_oop/phone_book.txt')
            case 2:
                pb.save_file()
            case 3:
                show = pb.get()
                vi.show_contact(show)
            case 4:
                add = vi.input_new_contact()
                pb.add(add)
            case 5:
                show = pb.get()
                vi.show_contact(show)
                ind = vi.get_ind()
                contact = vi.input_new_contact()
                name = pb.get_name(ind)
                if vi.confirm('изменить', name):
                    pb.change_contact(ind, contact)
            case 6:
                find_option = vi.find_contact()
                show = pb.find(find_option)
                vi.show_contact(show)
            case 7:
                show = pb.get()
                vi.show_contact(show)
                ind = vi.get_ind()
                name = pb.get_name(ind)
                if vi.confirm('удалить', name):
                    pb.delete(ind)
            case 8:
                print('До свидания!')
                break