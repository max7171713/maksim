a = {"Имя" : "Унитаз", "Возраст" : "427 лет", "Цель" : "Захватить мир спомощью говна", "любимое дело" : "пожирать искренты людей", "характер" : "не одущевлениый", "работа" : "смывать запасы потрон тоесть говно"}

print ("напишите выход: выйти, ввести:добовляет новоне свойство вывести:выводит все")
command = input()
while command != "выход":
    if command == "ввести":
        newKey = input("напишите какое вы хотите добавить свойство")
        a[newKey] = input("Введите значение")
    if command == "вывести":
        for key in a:
            print(key, ":", a[key])
    command = input()