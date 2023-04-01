a = {"имя" : "Максим","фамилия" : "Юхлин","отчество" : "Владимeрович"}
print ("напишите выход: выйти, ввести:добовляет новый предмет вывести:выводит все")
command = input()
while command != "выход":
    if command == "ввести":
        newKey = input("напишите какое вы хотите добавить свойство")
        a[newKey] = input("Введите значение")
    if command == "убрать":
        delKey = input("напишите какое вы хотите убрать придмет")
        a.pop(delKey, None)
    if command == "вывести":
        for key in a:
            print(key, ":", a[key])
    command = input()