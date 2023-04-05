def mat(op, x):
    print(op(x))

# def calc1(a):
    # return a+a

# calc1 = lambda a: a + a

# mat(calc1, 5)

mat(lambda a: a + a, 5)

def calc2(a):
    return a*a

mat(calc2, 5)

