a=["литература","алгебра","русский","англиский","физика","физ-ра","общества знание"]
myList=["геометрия","физика","литература"]
print("ваша задача собрать рюкзак пожулуйста помогите гене")
command = input()
while command != "закончить игру":
    if command == "показать уроки":
        print(a)
    if command == "показать рюкзак":
        print(myList)
    elif command == "выкинуть урок":
        print(myList)
        i =int(input("выберите учебник который хотите выкинуть(тоесть индекс)"))
        del myList[i]
        print(myList)
    elif command == "добавить в рюкзак урок":
        myList.insert(1,input("напишите какой вы хотите добавить в рюкзак урок"))
        print(myList)
    command = input()
    
    