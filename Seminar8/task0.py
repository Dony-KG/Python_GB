# Составить телефонный справочник/
# 1. Открыть файл
# 2. Сохранить файл
# 3. Просмотреть контакты
# 4. Создать контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выходu

def show_phonebook():
    file = open('D:\GB\ phonebook.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    for i in data:
        print(i)
    file.close()

def create_contact():
    file = open('D:\GB\ phonebook.txt', 'a', encoding='UTF-8')
    data = input('Введите данные ФИО, телефон, комментарий (через ;)')
    file.write('\n'+data)
    file.close()


def find_contact(find_data):
    file = open('D:\GB\ phonebook.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    for item in data:
        if find_data in item:
            print(item)
    file.close()

def del_contact(find_data):
    file = open('D:\GB\ phonebook.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    for item in data:
        if find_data in item:
            data.remove(item)
    print(data)
    file.close()

print('Главное меню\n''1. Просмотреть контакты\n''2. Создать контакт\n''3. Найти контакт\n''4. Изменить контакт\n''5. Удалить контакт\n''6. Выход\n')

choose = int(input("Выберите пункт: "))

if choose == 1:
    show_phonebook()

if choose == 2:
    create_contact()

if choose == 3:
    find = input()
    find_contact(find)

if choose == 5:
    find = input()
    del_contact(find)