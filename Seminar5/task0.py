def fib (number):
    if number == 1 or number == 2:
        return 1
    return (fib(number - 1) + fib(number - 2))


print(fib(10))