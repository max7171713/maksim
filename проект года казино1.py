import tkinter as tk
def kazik():
    b.pack_forget()
    n.pack_forget()
    
    o = input_console.get()
    o = int()
    if o <= 100:
        ui("вы пойманы")

def ui(output):
    console.insert(tk.END, output + "\n")

a = tk.Tk()
a.title("казино")

b = tk.Label(a,text = "вход в казино")
b.pack()

n = tk.Button(a,text = "зайти", command = kazik)
n.pack()

console = tk.Text(a, width=40, height=10)
console.pack()

input_console = tk.Entry(a)
input_console.bind("<Return>", kazik)
input_console.pack()

a.mainloop()
