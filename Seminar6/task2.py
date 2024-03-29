# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1,
# но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите
# все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное число k,
# не превосходящее 105. Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз
# (перестановка чисел новую пару не дает).

def sum_divisors(n):
    divisors = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors += i + n // i
    return divisors


k = int(input('Введите число: '))
dict_divisors = {}
for i in range(1, k):
    dict_divisors[i] = sum_divisors(i)

list_1 = []
for key, value in dict_divisors.items():
    if dict_divisors.get(dict_divisors.get(key)) == key and key != value:
        if (value, key) not in list_1:
            list_1.append((key, value))

print(list_1)