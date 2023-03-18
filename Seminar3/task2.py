# Дана упорядоченная последовательность an чисел от 1 до N. Из копии данной последовательности
# bn удалили одно число, а оставшиеся перемешали. Найти удаленное число.

import random

my_list = [i for i in range(10)]
print(my_list)
my_set = set(my_list)

my_list.pop(random.randint(0, 9))

random.shuffle(my_list)
print(my_list)

change_set = set(my_list)


print(*my_set.difference(change_set))
