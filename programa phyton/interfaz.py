import tkinter as tk

def saludar():
    nombre = entrada_nombre.get()
    mensaje = "¡Hola, {}!".format(nombre)
    etiqueta_saludo.config(text=mensaje)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Saludo")

# Crear un marco para contener los elementos
marco = tk.Frame(ventana)
marco.pack(padx=10, pady=10)

# Crear una etiqueta y un campo de entrada
etiqueta_nombre = tk.Label(marco, text="Nombre:")
etiqueta_nombre.grid(row=0, column=0, sticky="w")

entrada_nombre = tk.Entry(marco)
entrada_nombre.grid(row=0, column=1)

# Crear un botón
boton_saludar = tk.Button(marco, text="Saludar", command=saludar)
boton_saludar.grid(row=1, columnspan=2)

# Crear una etiqueta para mostrar el saludo
etiqueta_saludo = tk.Label(marco, text="")
etiqueta_saludo.grid(row=2, columnspan=2)

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()