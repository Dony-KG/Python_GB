import text_fields as txt


def main_menu() -> int:
    print(txt.main_menu)
    choice = ''
    while True:
        choice = input(txt.choice_menu)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)
        else:
            print(txt.input_num_menu)


def print_info(message: str):
    print('\n' + '-' * len(message))
    print(message)
    print('-' * len(message) + '\n')


def show_contact(book: list, message: str):
    if book:
        print('\n' + '-' * 70)
        for n, contact in enumerate(book, 1):
            print(f'{n:>3}. {contact.get("name"):<20}'
                  f'{contact.get("phone"):<20}'
                  f'{contact.get("comment"):<20}')
        print('-' * 70 + '\n')
    else:
        print(message)


def new_contact() -> dict:
    print()
    name = input(txt.new_name)
    phone = input(txt.new_phone)
    comment = input(txt.new_comment)
    print()
    return {'name': name, 'phone': phone, 'comment': comment}


def input_find_contact() -> str:
    print()
    contact = (input(txt.find_word))
    return contact


def print_find_contact(find_contact):
    print('\n' + '-' * 70)
    print(txt.find_count, end=' ')
    print(len(find_contact))
    print('-' * 70)
    for n, item in enumerate(find_contact, 1):
        print(f'{n:>3}. {item.get("name"):<20}'
              f'{item.get("phone"):<20}'
              f'{item.get("comment"):<20}')
    print('-' * 70 + '\n')


def print_change_contact() -> int:
    point = int(input(txt.change_contact_info))
    return point


def change_contact(contact: dict) -> list:
    print(*contact)
    point = []
    point.append(input(txt.change_contact))
    point.append(input(txt.change_data_info))
    return point

def print_del_contact() ->int:
    point = int(input(txt.del_contact_info))
    return point

def confirm(message) -> bool:
    answer = input(message + 'y/n: ')
    if answer.lower() == 'y':
        return True
    else:
        return False
