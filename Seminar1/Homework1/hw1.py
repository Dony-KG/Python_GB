# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

all_shadoof = int(input("Введите общее количество сделанных журавликов: "))
if all_shadoof % 3 ==0:
    if all_shadoof // 3 % 2 == 0:
        print(f"Петя и Сережа сделали по {all_shadoof // 3 // 2} журавлику(ов), а Катя {all_shadoof // 3 * 2} журавликов")
    else:
        print("Общее количество журавликов не соответсвует условию задачи")
else:
    print("Общее количество журавликов не соответсвует условию задачи")