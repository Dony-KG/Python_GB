# В списке хранятся числа. Нужно выбрать только четные числа и составить список пар(число; квадрат числа)

my_list = [1, 2, 3, 5, 8, 15, 23, 38]


# new_list = []
# for i in my_list:
#     if i%2 == 0:
#         new_list.append(i, i**2))
#
# print(new_list)

# def select(f, col):             #map то что и выполняет select
#     return [f(x) for x in col]


# def where(f, col):                #filter то что и выполняет where
#     return [x for x in col if f(x)]


new_list = map(int, my_list)

new_list = filter(lambda x: x % 2 == 0, new_list)

new_list = list(map(lambda x: (x, x**2), new_list))
print(new_list)