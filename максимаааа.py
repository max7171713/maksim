import random
bot=[["*","*","*","*","*","*","$","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*"],
        ["*","*","$","*","*","*","$","*","*","*"],
        ["*","*","*","$","$","*","*","*","*","*"],
        ["*","*","*","*","*","*","$","$","$","*"],
        ["*","*","*","*","*","*","*","*","*","*"],
        ["*","*","$","*","*","*","*","$","$","*"],
        ["*","*","*","*","*","$","*","*","*","*"],
        ["*","*","*","*","*","$","*","$","*","*"],
        ["$","$","$","$","*","$","*","$","*","*"]]


bot2=[["*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*"]]

player=[["*","*","*","*","*","*","*","*","*","*"],
        ["*","$","*","*","*","*","$","*","$","*"],
        ["*","*","*","$","*","*","$","*","*","*"],
        ["*","*","*","$","*","*","$","*","*","*"],
        ["*","*","*","$","*","*","*","*","$","*"],
        ["*","$","*","*","*","*","*","*","$","*"],
        ["*","*","*","$","*","$","$","*","*","*"],
        ["*","*","*","$","*","*","*","*","*","*"],
        ["*","*","*","$","*","*","$","$","*","*"],
        ["$","*","*","$","*","*","*","*","*","*"]]
hpbot = 20
hpplayer = 20
command = input()
stroka = 0
stolbec = 0
while command !="закончить":
    if command == "враг":
        for i in bot2:
            for j in i:
                print(j, end='')
            print()
    if command == "я":
        for i in player:
            for j in i:
                print(j, end='')
            print()
    if command == "стрелять":
        stroka = int(input())
        stolbec = int(input())
        if bot[stroka][stolbec] == "$":
            bot[stroka][stolbec]="#"
        else:
            bot[stroka][stolbec]="O" 
        a = random.randint(0,9)
        b = random.randint(0,9)
        if player[b][a] == "$":
            player[b][a]="#"
            print("враг-попало")
            hpplayer -=1
        else:
            player[b][a]="O" 
            print("враг-мимо")
        if stroka == 0 and stolbec == 6: 
            bot2[stroka][stolbec]="#"
            print("вы-попало")
            hpbot +=1
        elif stroka == 2 and stolbec == 2: 
            bot2[stroka][stolbec]="#"
            print("вы-попало")
            hpbot +=1
        elif stroka == 2 and stolbec == 6: 
            bot2[stroka][stolbec]="#"
            print("вы-попало")
            hpbot +=1
        elif stroka == 3 and stolbec == 3: 
            bot2[stroka][stolbec]="#"
            print("вы-попало")
            hpbot +=1
        elif stroka == 3 and stolbec == 4: 
            bot2[stroka][stolbec]="#"
            print("вы-попало")
            hpbot +=1
        elif stroka == 4 and stolbec == 6: 
            bot2[stroka][stolbec]="#"
            print("вы-попало")
            hpbot +=1
        elif stroka == 4 and stolbec == 7: 
            bot2[stroka][stolbec]="#"
            print("вы-попало")
            hpbot +=1
        elif stroka == 4 and stolbec == 8: 
            bot2[stroka][stolbec]="#"
            print("вы-попало")
            hpbot +=1
        elif stroka == 6 and stolbec == 2: 
            bot2[stroka][stolbec]="#"
            print("вы-попало")
            hpbot +=1
        elif stroka == 6 and stolbec == 7: 
            bot2[stroka][stolbec]="#"
            print("вы-попало")
            hpbot +=1
        elif stroka == 6 and stolbec == 8: 
            bot2[stroka][stolbec]="#"
            print("вы-попало")
            hpbot +=1
        elif stroka == 7 and stolbec == 5: 
            bot2[stroka][stolbec]="#"
            print("вы-попало")
            hpbot +=1
        elif stroka == 8 and stolbec == 5: 
            bot2[stroka][stolbec]="#"
            print("вы-попало")
            hpbot +=1
        elif stroka == 8 and stolbec == 7: 
            bot2[stroka][stolbec]="#"
            print("вы-попало")
            hpbot +=1
        elif stroka == 9 and stolbec == 0: 
            bot2[stroka][stolbec]="#"
            print("вы-попало")
            hpbot +=1
        elif stroka == 9 and stolbec == 1: 
            bot2[stroka][stolbec]="#"
            print("вы-попало")
            hpbot +=1
        elif stroka == 9 and stolbec == 2: 
            bot2[stroka][stolbec]="#"
            print("вы-попало")
            hpbot +=1
        elif stroka == 9 and stolbec == 3: 
            bot2[stroka][stolbec]="#"
            print("вы-попало")
            hpbot +=1
        elif stroka == 9 and stolbec == 5: 
            bot2[stroka][stolbec]="#"
            print("вы-попало")
            hpbot +=1
        elif stroka == 9 and stolbec == 7: 
            bot2[stroka][stolbec]="#"
            print("вы-попало")
            hpbot +=1
        else:
            bot2[stroka][stolbec]="O" 
            print("вы-мимо")
        if hpbot == 40:
            print("ты выиграл")
        elif hpplayer == 0:
            print("ты проиграл")
    command = input()