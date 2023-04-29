from tkinter import*
def jmyak():
    lbl.configure(text = "Лол говорит:зачем ты это сделал ты убил мою семью неееееет <=(!!")
window = Tk()
window.title("дом лол")
window.geometry('2030x2030')
lbl = Label(window,text = "привет я лол и пожалуйста не нажимай на кнопку",font = ("Arial Blod",35))
lbl.pack()
btn= Button(window,text="нажми нажми на меня >=)",command = jmyak)
btn.pack()






window.mainloop()