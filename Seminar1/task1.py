# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.

import math

class_1 = int(input("Введите количество учеников 1 класса: "))
class_2 = int(input("Введите количество учеников 2 класса: "))
class_3 = int(input("Введите количество учеников 3 класса: "))

print(math.ceil(class_1 / 2) + math.ceil(class_2 / 2) + math.ceil(class_3 / 2))
