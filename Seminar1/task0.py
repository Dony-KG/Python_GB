# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

route_length = int(input("Введите длину маршрута: "))

route_length_day = int(input("Введите сколько проезжает машина в день: "))

print(int((route_length + route_length_day - 1) / route_length_day))
