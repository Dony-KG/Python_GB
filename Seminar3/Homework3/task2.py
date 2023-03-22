#  В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. В случае с английским алфавитом очки
#  распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка;
#  K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
#  Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков;
#  Ф, Щ, Ъ – 10 очков. Напишите программу, которая вычисляет стоимость введенного пользователем слова.
#  Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
#  либо только русские буквы.

list1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
list2 = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
list3 = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
list4 = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
list5 = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
list8 = ['J', 'X', 'Ш', 'Э', 'Ю']
list10 = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']

count = 0

word = input("Введите слово: ")
word = list(word.upper())
for i in range(len(list1)):
    count += word.count(list1[i])

for i in range(len(list2)):
    count += word.count(list2[i])*2

for i in range(len(list3)):
    count += word.count(list3[i])*3

for i in range(len(list4)):
    count += word.count(list4[i])*4

for i in range(len(list5)):
    count += word.count(list5[i])*5

for i in range(len(list8)):
    count += word.count(list8[i])*8

for i in range(len(list10)):
    count += word.count(list10[i])*10

print(count)
