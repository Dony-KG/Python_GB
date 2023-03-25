def summ (numb):
    if numb == 0:
        return 0
    return numb+summ(numb-1)


print(summ(9))