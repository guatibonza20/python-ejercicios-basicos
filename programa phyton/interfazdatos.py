import tkinter as tk

def imprimir_datos():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    print("Nombre:", nombre)
    print("Apellido:", apellido)


root = tk.Tk()
root.title("Formulario de Datos")

label_nombre = tk.Label(root, text="Nombre:")
label_nombre.pack()


entry_nombre = tk.Entry(root)
entry_nombre.pack()

label_apellido = tk.Label(root, text="Apellido:")
label_apellido.pack()


entry_apellido = tk.Entry(root)
entry_apellido.pack()


boton_imprimir = tk.Button(root, text="Imprimir Datos", command=imprimir_datos)
boton_imprimir.pack()


root.mainloop()   