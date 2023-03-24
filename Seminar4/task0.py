# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n
import random
import string

in_str = input('Введите строку: ')
my_dict = {}

for i in in_str:
    if i in my_dict:
        print(f'{i}_{my_dict[i]}', end=' ')
        my_dict[i] += 1
    else:
        my_dict[i] = 1
        print(i, end=' ')
print()

in_str = ''.join(random.choice(string.ascii_letters) for _ in range(30))

dict_count = {}
for char in in_str:
    dict_count[char] = dict_count.get(char, 0) + 1
    if dict_count[char] > 1:
        print(f'{char}_{dict_count.get(char)}', end=' ')

    else:
        print(char, end=' ')
