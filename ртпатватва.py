slova = ["#", "#", "/", "#", "#", "#", "/", "#", "#",]
h=0
y=1
p=-1
e=-2

print(slova)
g=input("куда ствинуть вправо лево стоп и прыжок он делает 2 шага может перепрыгивать через стены когда ты перепрыгнишь стену она разрушица у тебя пять ходов 5 ")
for t in range(5):
    if g=="вправо":
        h=h+1
        p=p+1
        e=e+1
        slova[6]="/"
        slova[2]="/"
        slova[p]="#"
        slova[e]="#"
        slova[y]="#"
        slova[h]="*"        
        print(slova)
        print(h)
        g=input("куда ствинуть вправо лево стоп и прыжок он делает 2 шага может перепрыгивать через стены")
    elif h >= 7:
        print("победа")
    elif g=="лево":
        h=h-1
        p=p-1
        e=e-1
        slova[6]="/"
        slova[2]="/"
        slova[p]="#"
        slova[y]="#"
        slova[e]="#"
        slova[h]="*"       
        print(slova)
        print(h)
        g=input("куда ствинуть вправо лево стоп и прыжок он делает 2 шага может перепрыгивать через стены")
        
    elif g=="прыжок":
        h=h+2
        e=e+2
        p=p+2
        slova[6]="/"
        slova[2]="/"
        slova[p]="#"
        slova[y]="#"
        slova[e]="#"
        slova[h]="*"
        print(slova)
        print(h)
        g=input("куда ствинуть вправо лево стоп и прыжок он делает 2 шага может перепрыгивать через стены")           
    elif g=="стоп":
        slova[h]="*"        
        print(slova)
        ПРИВЕТТТТ

  






  





