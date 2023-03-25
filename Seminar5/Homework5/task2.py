# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
import math


def simple_number(number) -> int:
    if number in [1,2,3]:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number))+1, 2):
        if number % i == 0:
            return False
    return True



print(simple_number(30))
print(simple_number(81))
print(simple_number(17))

