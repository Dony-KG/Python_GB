from random import randint

days = int(input("Введите количество дней: "))
day_count = 1
max_day_count = 1
count = 0
current_day = 0
last_day = 0
while count < days:
    current_day = randint(-3, 3)
    if last_day > 0 and current_day > 0:
        day_count += 1
    else:
        day_count = 1
    if day_count > max_day_count:
        max_day_count = day_count
    count += 1
    last_day = current_day
    print(current_day, end=", ")

print()
print(f"Самая длинная оттепель за {days} дней, длилась {max_day_count} дней")
