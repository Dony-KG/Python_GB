# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь
# в первой строке вводит натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
list_length = int(input("Введите длину списка: "))
my_list = [random.randint(0, 10) for i in range(list_length)]
print(my_list)

find_number = int(input("Введите число которое нужно найти: "))

count = 0
for i in range(list_length):
    if my_list[i] == find_number:
        count += 1

print(f"Число {find_number} встречается {count} раз(а)")