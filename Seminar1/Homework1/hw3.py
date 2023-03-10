# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом
# по прямой между дольками (то есть разломить шоколадку на два прямоугольника

chocolate_length = int(input("Ввведите длину плитки шоколада: "))
chocolate_width = int(input("Ввведите ширину плитки шоколада: "))

a_slice_of_chocolate = int(input("Ввведите количество долек шоколада: "))
if a_slice_of_chocolate < chocolate_length * chocolate_width and (
        a_slice_of_chocolate % chocolate_length == 0 or a_slice_of_chocolate % chocolate_width == 0):
    print("Да, можно разломить")
else:
    print("Нет, нельзя разломить")
