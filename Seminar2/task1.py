# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.



fib_1, fib_2 = 1, 1
index = 1

while fib_2 <= numb:
    fib_1 += fib_2
    fib_1, fib_2 = fib_2, fib_1
    index += 1
    print(fib_1)

if fib_1 == numb:
    print(f"index = {index}")
else:
    print("-1")
