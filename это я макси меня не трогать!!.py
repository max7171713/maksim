myList=[["О","*","*","|","*","*","*","*","*"],["-","-","*","|","*","*","*","*","*"],["*","|","*","|","*","*","*","*","*"],["-","-","*","|","*","*","*","*","*"],["*","*","*","|","*","*","*","*","*"],["-","-","*","|","*","*","*","*","*"],["*","|","*","-","-","-","-","-","-"],["*","|","*","*","*","*","*","*","*"],["*","|","*","-","-","-","-","-","-"],["*","|","*","|","*","*","*","*","*"]]
command = input()
stroka = 0
stolbec = 0
while command !="закончить":
    if command == "показать О":
        for i in myList:
            for j in i:
                print(j, end='')
            print()
    if command == "переместить О":
        commandForMove = input()
        if commandForMove == "вверх":
            if myList[stolbec-1][stroka]=="|":
                myList[stolbec][stroka]="*"
                stroka=0
                stolbec=0
                myList[stolbec][stroka]="O"
            else:
                myList[stolbec][stroka]="*"
                stolbec=stolbec-1
                myList[stolbec][stroka]="O"
            for i in myList:
                for j in i:
                    print(j, end='')
                print()
        if commandForMove == "влего":
            if myList[stolbec][stroka+1]=="|":
                myList[stolbec][stroka]="*"
                stroka=0
                stolbec=0
                myList[stolbec][stroka]="O"
            else:
                myList[stolbec][stroka]="*"
                stroka=stroka+1
                myList[stolbec][stroka]="O"
            for i in myList:
                for j in i:
                    print(j, end='')
                print()
        if commandForMove == "вниз":
            if myList[stolbec+1][stroka]=="|":
                myList[stolbec][stroka]="*"
                stroka=0
                stolbec=0
                myList[stolbec][stroka]="O"
            else:
                myList[stolbec][stroka]="*"
                stolbec=stolbec+1
                myList[stolbec][stroka]="O"
            for i in myList:
                for j in i:
                    print(j, end='')
                print()
        if commandForMove == "впраго":
            if myList[stolbec][stroka-1]=="|":
                myList[stolbec][stroka]="*"
                stroka=0
                stolbec=0
                myList[stolbec][stroka]="O"
            else:
                myList[stolbec][stroka]="*"
                stroka=stroka-1
                myList[stolbec][stroka]="O"
            for i in myList:
                for j in i:
                    print(j, end='')
                print()
        if stolbec == 7 and stroka == 7:
            print("ты победил")
    command = input()
            