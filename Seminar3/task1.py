# Дан список, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов списка,
# больших предыдущего (элемента с предыдущим номером)
import random

my_list = [random.randint(0, 20) for i in range(0, 15)]
print(my_list)
count = 0
for i in range(1, len(my_list)):
    if my_list[i-1] < my_list[i]:
        count += 1

print(count)
