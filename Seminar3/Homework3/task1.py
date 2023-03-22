#  Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь
#  в первой строке вводит натуральное число N – количество элементов в массиве.
#  В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

list_length = int(input("Введите длину списка: "))
my_list = [random.randint(1, 20) for i in range(list_length)]
print(my_list)

flag = True
find_number = int(input("Введите число: "))
number =find_number
count = 1
while flag:
    for i in range(list_length):
        if my_list[i] == find_number:
            print(f"Число {my_list[i]} самый близкий к {number}")
            flag = False
            break

    if count % 2 == 0:
        find_number += count
    else:
        find_number -= count
    count += 1
