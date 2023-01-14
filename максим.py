command = input()
myList=["геометрия","физика","литература"]
while command != "конец":
    if command == "показать список":
        print(myList)
    elif command == "удалить":
        i =int(input("выберите индекс который хотите удалить"))
        del myList[i]
        print(myList)
    elif command == "показать список по индексу":
        i =int(input("выберете индекс который хотите увидеть"))
        print(myList[i])
    elif command == "добавить в список":
        print(myList)
        myList.insert(1,input("передвами недавно появился список напишите что вы хотите добавить в него"))
    command = input()