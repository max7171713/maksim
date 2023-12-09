import random
import time

# Поле
a = [["v", "|", "v", "|", "v"],
     ["v", "|", "v", "|", "v"],
     ["v", "|", "v", "|", "v"]]

# Функция для проверки победы
def check_win():
    # Горизонтальные и вертикальные комбинации
    for i in range(3):
        if a[i][0] != "v" and a[i][0] == a[i][2] == a[i][4]:
            return a[i][0]
        if a[0][i] != "v" and a[0][i] == a[1][i] == a[2][i]:
            return a[0][i]

    # Диагональные комбинации
    if a[0][0] != "v" and a[0][0] == a[1][2] == a[2][4]:
        return a[0][0]
    if a[0][4] != "v" and a[0][4] == a[1][2] == a[2][0]:
        return a[0][4]

    return None

# Начальный текст
print("вы: это вы (логично)")
time.sleep(3)
print("враг: это враг (тоже логично)")
time.sleep(3)
print("v: пусто")
time.sleep(2)
print("d: враг")
time.sleep(2)
print("n: вы")
time.sleep(2)
print("подождите идет загрузка")
time.sleep(4)
print("это игра крестики-нолики")
print("выход")
print("играть")

command = input()
while command != "выход":
    if command == "играть":
        print("выводим ваше поле")
        for i in a:
            for j in i:
                print(j, end='')
            print()
        print("вы можете ход,вывести или выйти")
        command = input()
    # команда на ходы
    if command == "ход":
        stroka = int(input("Введите номер строки: "))
        stolbec = int(input("Введите номер столбца: "))
        if a[stroka][stolbec] == "v":
            a[stroka][stolbec] = "n"
    else:
        c = random.randint(0, 2)
        b = random.randrange(0, 6, 2)
        a[b][c] = "v"
        a[b][c] = "d"
    # команда на выведение поля
    if command == "вывести":
        for i in a:
            for j in i:
                print(j, end='')
            print()
    command = input()