from tkinter import*
def jmyak():
    lbl.configure(text = ent.get())
window = Tk()
window.title("дом лол")
window.geometry('2030x2030')
lbl = Label(window,text = "привет я лол и пожалуйста не нажимай на кнопку",font = ("Arial Blod",35))
lbl.pack()
btn= Button(window,text="нажми нажми на меня >=)",command = jmyak)
btn.pack()
ent = Entry(window,width = 100)
newText = ent.get()
ent.pack()






window.mainloop()