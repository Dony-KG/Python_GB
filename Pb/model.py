phone_book = []
start_phone_book = []
PATH = "phone_book.txt"


def get_pb():
    return phone_book


def load_file():
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(';')
        phone_book.append({'name': contact[0],
                           'phone': contact[1],
                           'comment': contact[2]})
    start_phone_book = phone_book.copy()


def save_file():
    data = []
    for contact in phone_book:
        data.append(';'.join(value for value in contact.values()))
    data = '\n'.join(data)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(data)


def add_contact(contact: dict):
    phone_book.append(contact)


def find_in_phone_book(find_data: str) -> list:
    found_data = []
    for data in phone_book:
        for item in data.values():
            if find_data.lower() in item.lower():
                found_data.append(data)
    return found_data


def find_for_change_phone_book(change_data: int) -> dict:
    for n, item in enumerate(phone_book, 1):
        if n == change_data:
            return item.values()


def change_phone_book(change_data: list, point: int):
    match int(change_data[0]):
        case 1:
            phone_book[point - 1]['name'] = change_data[1]
        case 2:
            phone_book[point - 1]['phone'] = change_data[1]
        case 3:
            phone_book[point - 1]['comment'] = change_data[1]

def del_phone_book(point):
    for n, item in enumerate(phone_book, 1):
        if n == point:
            phone_book.remove(item)


def exit_pb() -> bool:
    if phone_book == start_phone_book:
        return False
    else:
        return True
