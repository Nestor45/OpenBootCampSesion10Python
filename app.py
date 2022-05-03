from gc import callbacks
from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()

seleccionado = StringVar()

def seleccion_combobox(event):
    messagebox.showinfo(
        title="Nuevo elemento seleccionado",
        message=f"Selecciono {seleccionado.get()}"
    )

ttk.Label(frm,text="Seleccione una opción del Combo").grid(column=0, row=1)
combo = ttk.Combobox(frm,values=['Python', 'Java', 'PHP'], textvariable=seleccionado, state="readonly")
combo.grid(column=0, row=2)
combo.bind('<<ComboboxSelected>>', seleccion_combobox)

root.mainloop()