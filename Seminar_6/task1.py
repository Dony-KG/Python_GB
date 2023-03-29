# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного

import random

length = int(input("Введите длину списка: "))

my_list = [random.randint(1, 10) for i in range(length)]
print(my_list)

count = 0
for i in range(length):
    if my_list[i - 2] < my_list[i - 1] > my_list[i]:
        count += 1

print(count)

count = 0
for i in range(length):
    if my_list[i%length-2] < my_list[i%length - 1] > my_list[i%length]:
        count += 1

print(count)