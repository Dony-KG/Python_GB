# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

numb = int(input("Введите число: "))
flag = 0

rate = 1

while flag == 0:
    if numb > 2 ** rate:
        print(2 ** rate, end=" ")
        rate += 1
    else:
        flag = 1
