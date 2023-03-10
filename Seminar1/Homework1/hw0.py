# Найдите сумму цифр трехзначного числа.

number = int(input("Введите трехзначное число: "))

summ = number % 10
number = number // 10
summ = summ + number % 10
number = number // 10
summ = summ + number % 10

print(f'Сумма цифр числа равно: {summ}')
