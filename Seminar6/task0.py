# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в
# первом массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве,
# затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
import random

val = list(map(int, input("Введите длину двух списков, и минимум и максимум значений,через пробел ").split()))

list_1 = [random.randint(val[2], val[3]) for _ in range(val[0])]
list_2 = [random.randint(val[2], val[3]) for _ in range(val[1])]
print(list_1)
print(list_2)


list_3 = [i for i in list_1 if i not in list_2]

print(list_3)

for i in list_1:
    if i not in list_2:
        print(i, end=' ')