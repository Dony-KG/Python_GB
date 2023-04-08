import random


def find_farthest_orbit(list_of_orbits):
    new_list = list(filter(lambda x: x[0] != x[1], list_of_orbits))
    mult_list = list(map(lambda x: x[0] * x[1], new_list))
    return new_list[mult_list.index(max(mult_list))]


ellipsis_of_orbits = [(random.randint(1, 10), random.randint(1, 10)) for _ in range(10)]

print(ellipsis_of_orbits)

print(*find_farthest_orbit(ellipsis_of_orbits))
