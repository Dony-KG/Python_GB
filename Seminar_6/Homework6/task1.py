# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно
# ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first = int(input('Введите первый элемент прогрессии: '))
length = int(input('Введите длину прогрессии: '))
difference = int(input('Введите разность прогрессии: '))

list_1 = []
list_2 = []
list_1.append(first)
for i in range(1, length):
    list_1.append(list_1[i - 1] + difference)

print(list_1)

for i in range(length):
    list_2.append(first + i * difference)
print(list_2)