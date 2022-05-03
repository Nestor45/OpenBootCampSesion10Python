from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()

seleccionado = StringVar()
seleccionado.set(None)

def seleccion():
    match seleccionado.get():
        case '1':
            messagebox.showinfo("","Radiobutton1")
        case '2':
            messagebox.showinfo("","Radiobutton2")
        case '3':
            messagebox.showinfo("","Radiobutton3")
        case '4':
            messagebox.showinfo("","Radiobutton4")

def reset():
    seleccionado.set(None)


imprimir1 = "Hello World!"
mostrar = ttk.Label(frm, text=imprimir1).grid(column=0, row=0)


ttk.Radiobutton(frm,text='Radiobutton1', value='1', variable=seleccionado,command=seleccion).grid(column=0, row=2)
ttk.Radiobutton(frm,text='Radiobutton2', value='2', variable=seleccionado,command=seleccion).grid(column=1, row=2)
ttk.Radiobutton(frm,text='Radiobutton3', value='3', variable=seleccionado,command=seleccion).grid(column=2, row=2)
ttk.Radiobutton(frm,text='Radiobutton4', value='4', variable=seleccionado,command=seleccion).grid(column=3, row=2)



ttk.Button(frm,state=True,text="Salir", command=root.destroy).grid(column=0, row=6)
ttk.Button(frm,state=True,text="Reset", command=reset).grid(column=1, row=6)



root.mainloop()