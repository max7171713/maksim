c = ["молоко", "пирог", "робот убийца", "консоль", "хлеб"]
print("Вот ваш список:", c)
a = input(f"Вот ваше слово из списка {c[0]} хотите ли вы его заменить?")
if a == "да":
    b = input("и на что же?")
    c[0]=b
    print("вот ваш список:",c)
else:
    print("")
a = input(f"Вот ваше слово из списка {c[1]} хотите ли вы его заменить?")
if a == "да":
    b = input("и на что же?")
    c[1]=b
    print("вот ваш список:",c)
else:
    print("")
a = input(f"Вот ваше слово из списка {c[2]} хотите ли вы его заменить?")
if a == "да":
    b = input("и на что же?")
    c[2]=b
    print("вот ваш список:",c)
else:
    print("")
a = input(f"Вот ваше слово из списка {c[3]} хотите ли вы его заменить?")
if a == "да":
    b = input("и на что же?")
    c[3]=b
    print("вот ваш список:",c)
else:
    print("")
a = input(f"Вот ваше слово из списка {c[4]} хотите ли вы его заменить?")
if a == "да":
    b = input("и на что же?")
    c[4]=b
    print("вот ваш список:",c)
else:
    print("лады пока")