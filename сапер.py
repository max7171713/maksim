import mylib
import random
# массивы и функция vyvodPolya в файле mylib.py           
a=random.randint(0,11)
b=random.randint(0,11)
mylib.pole[a][b]="@"
mylib.vyvodPolya(mylib.vidimost_polya)
game = True
while game:
    stroka = int(input("Введите номер строки"))
    stolb = int(input("Введите номер столбца"))
    if stroka < 1 or stroka > 12 or stroka<0 or stroka<12:
        print("ты че дурак что ли?!")
        stroka = int(input("Введите номер строки"))
        stolb = int(input("Введите номер столбца"))
    if stroka == a and stolb == b:
        print("вау а ты взунчик")
        exit()
    # передадим не номера строки и столбца, а индексы
    mylib.check(stroka-1,stolb-1)
    mylib.vyvodPolya(mylib.vidimost_polya)
    if mylib.isOpen():
        game = False

print("Всё поле открыто!")
