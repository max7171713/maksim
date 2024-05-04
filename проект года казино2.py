import tkinter as tk
def kazik(event):
    
    o = input_console.get()
    o = int()
    if o <= 100:
        ui("вы пойманы")

def ui(output):
    console.insert(tk.END, output + "\n")

a = tk.Tk()
a.title("казино")

console = tk.Text(a, width=40, height=10)
console.pack()

input_console = tk.Entry(a)
input_console.bind("<Return>", kazik)
input_console.pack()

a.mainloop()
