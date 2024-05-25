import tkinter as tk
import random
import time
balanse = 10000
yuy = 0
def kazik(event):
    global balanse
    global yuy
    
    console.delete('1.0', tk.END)
    o = int(input_console.get())
    if balanse <= 0:
        print("казино: вы можете оплатить свой проигрышь?")
        print("вы: лезете в карман а там пусто")
        print("казино:праваливайте от сюда!")
        exit("вас выгнали из казино")
    elif o <= 299:
        if yuy <= 0:
            oi("это казино тут есть ставки выигрышь проигрышь главное не потеряйте все деньги")
            oi(f"ваш баланс = {balanse}$")
            oi("максимум ставка 100000$ минимум 300$")
            oi("а так же будут шансы на выигрышь")
            yuy = yuy+1
        ui("простите но минимальная ставка это 300$")
    elif o > 40000:
        if yuy <= 0:
            oi("это казино тут есть ставки выигрышь проигрышь главное не потеряйте все деньги")
            oi(f"ваш баланс = {balanse}$")
            oi("максимум ставка 1000000$ минимум 300$")
            oi("а так же будут шансы на выигрышь")
            yuy = yuy+1
        if balanse < o:
            oi("простите но вы не можете поставить эту ставку")
        else:
            oi(f"ваша ставка = {o}$")
            g = random.randint(1,3)
            g = g*10
            opp = random.randint(1,10)
            oi(f"ваш шанс выиграть = {g}%")
            g = g/10
            if g == 1:
                if opp <= 1:
                    oi(f"вы выиграли {o*2}$!")
                    balanse = o*2+balanse
                    oi(f"ваш баланс = {balanse}$")
                else:
                    oi(f"вы проиграли {o}$")
                    balanse = balanse - o
                    oi(f"ваш баланс = {balanse}$")
            if g == 2:
                if opp <= 2:
                    oi(f"вы выиграли {o*2}$!")
                    balanse = o*2+balanse
                    oi(f"ваш баланс = {balanse}$")
                else:
                    oi(f"вы проиграли {o}$")
                    balanse = balanse - o
                    oi(f"ваш баланс = {balanse}$")
            if g == 3:
                if opp <= 3:
                    oi(f"вы выиграли {o*2}$!")
                    balanse = o*2+balanse
                    oi(f"ваш баланс = {balanse}$")
                else:
                    oi(f"вы проиграли {o}$")
                    balanse = balanse - o
                    oi(f"ваш баланс = {balanse}$")
                    
    elif o >= 1001 and o <= 40000:
        if yuy <= 0:
            oi("это казино тут есть ставки выигрышь проигрышь главное не потеряйте все деньги")
            oi(f"ваш баланс = {balanse}$")
            oi("максимум ставка 1000000$ минимум 300$")
            oi("а так же будут шансы на выигрышь")
            yuy = yuy+1
        if balanse < o:
            oi("простите но вы не можете поставить эту ставку")
        else:
            oi(f"ваша ставка = {o}$")
            g = random.randint(1,5)
            g = g*10
            opp = random.randint(1,10)
            oi(f"ваш шанс выиграть = {g}%")
            g = g/10
            if g == 1:
                if opp <= 1:
                    oi(f"вы выиграли {o*2}$!")
                    balanse = o*2+balanse
                    oi(f"ваш баланс = {balanse}$")
                else:
                    oi(f"вы проиграли {o}$")
                    balanse = balanse - o
                    oi(f"ваш баланс = {balanse}$")
            if g == 2:
                if opp <= 2:
                    oi(f"вы выиграли {o*2}$!")
                    balanse = o*2+balanse
                    oi(f"ваш баланс = {balanse}$")
                else:
                    oi(f"вы проиграли {o}$")
                    balanse = balanse - o
                    oi(f"ваш баланс = {balanse}$")
            if g == 3:
                if opp <= 3:
                    oi(f"вы выиграли {o*2}$!")
                    balanse = o*2+balanse
                    oi(f"ваш баланс = {balanse}$")
                else:
                    oi(f"вы проиграли {o}$")
                    balanse = balanse - o
                    oi(f"ваш баланс = {balanse}$")
            if g == 4:
                if opp <= 4:
                    oi(f"вы выиграли {o*2}$!")
                    balanse = o*2+balanse
                    oi(f"ваш баланс = {balanse}$")
                else:
                    oi(f"вы проиграли {o}$")
                    balanse = balanse - o
                    oi(f"ваш баланс = {balanse}$")
            if g == 5:
                if opp <= 5:
                    oi(f"вы выиграли {o*2}$!")
                    balanse = o*2+balanse
                    oi(f"ваш баланс = {balanse}$")
                else:
                    oi(f"вы проиграли {o}$")
                    balanse = balanse - o
                    oi(f"ваш баланс = {balanse}$")
            
    elif o >= 100001:
        if yuy <= 0:
            oi("это казино тут есть ставки выигрышь проигрышь главное не потеряйте все деньги")
            oi(f"ваш баланс = {balanse}$")
            oi("максимум ставка 100000$ минимум 300$")
            oi("а так же будут шансы на выигрышь")
            oi(f"ваш баланс = {balanse}$")
            yuy = yuy+1
        oi("простите но казино не принимает такие ставки")
     
    elif o >= 300 and o <= 1000:
        if yuy <= 0:
            oi("это казино тут есть ставки выигрышь проигрышь главное не потеряйте все деньги")
            oi(f"ваш баланс = {balanse}$")
            oi("максимум ставка 100000$ минимум 300$")
            oi("а так же будут шансы на выигрышь")
            oi(f"ваш баланс = {balanse}$")
            yuy = yuy+1
        if balanse < o:
            oi("простите но вы не можете поставить эту ставку")
        else:
            oi(f"ваша ставка = {o}$")
            g = random.randint(1,8)
            g = g*10
            opp = random.randint(1,10)
            oi(f"ваш шанс выиграть = {g}%")
            g = g/10
            if g == 1:
                if opp <= 1:
                    oi(f"вы выиграли {o*2}$!")
                    balanse = o*2+balanse
                    oi(f"ваш баланс = {balanse}$")
                else:
                    oi(f"вы проиграли {o}$")
                    balanse = balanse - o
                    oi(f"ваш баланс = {balanse}$")
            if g == 2:
                if opp <= 2:
                    oi(f"вы выиграли {o*2}$!")
                    balanse = o*2+balanse
                    oi(f"ваш баланс = {balanse}$")
                else:
                    oi(f"вы проиграли {o}$")
                    balanse = balanse - o
                    oi(f"ваш баланс = {balanse}$")
            if g == 3:
                if opp <= 3:
                    oi(f"вы выиграли {o*2}$!")
                    balanse = o*2+balanse
                    oi(f"ваш баланс = {balanse}$")
                else:
                    oi(f"вы проиграли {o}$")
                    balanse = balanse - o
                    oi(f"ваш баланс = {balanse}$")
            if g == 4:
                if opp <= 4:
                    oi(f"вы выиграли {o*2}$!")
                    balanse = o*2+balanse
                    oi(f"ваш баланс = {balanse}$")
                else:
                    oi(f"вы проиграли {o}$")
                    balanse = balanse - o
                    oi(f"ваш баланс = {balanse}$")
            if g == 5:
                if opp <= 5:
                    oi(f"вы выиграли {o*2}$!")
                    balanse = o*2+balanse
                    oi(f"ваш баланс = {balanse}$")
                else:
                    oi(f"вы проиграли {o}$")
                    balanse = balanse - o
                    oi(f"ваш баланс = {balanse}$")
            if g == 6:
                if opp <= 6:
                    oi(f"вы выиграли {o*2}$!")
                    balanse = o*2+balanse
                    oi(f"ваш баланс = {balanse}$")
                else:
                    oi(f"вы проиграли {o}$")
                    balanse = balanse - o
                    oi(f"ваш баланс = {balanse}$")
            if g == 7:
                if opp <= 7:
                    oi(f"вы выиграли {o*2}$!")
                    balanse = o*2+balanse
                    oi(f"ваш баланс = {balanse}$")
                else:
                    oi(f"вы проиграли {o}$")
                    balanse = balanse - o
                    oi(f"ваш баланс = {balanse}$")
            if g == 8:
                if opp <= 8:
                    oi(f"вы выиграли {o*2}$!")
                    balanse = o*2+balanse
                    oi(f"ваш баланс = {balanse}$")
                else:
                    oi(f"вы проиграли {o}$")
                    balanse = balanse - o
                    oi(f"ваш баланс = {balanse}$")
            
def ui(output):
    console.insert(tk.END, output + "\n")

def oi(output):
    console.insert(tk.END, output + "\n")
    
a = tk.Tk()
a.title("казино")

console = tk.Text(a, width=100, height=25)
console.pack()

input_console = tk.Entry(a)
input_console.bind("<Return>", kazik)
input_console.pack()

a.mainloop()
