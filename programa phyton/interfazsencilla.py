import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        if num2 != 0:
            division = num1 / num2
        else:
            division = "No se puede dividir por cero"
        
        resultado_suma.set(f"Suma: {suma}")
        resultado_resta.set(f"Resta: {resta}")
        resultado_multiplicacion.set(f"Multiplicación: {multiplicacion}")
        resultado_division.set(f"División: {division}")
        
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce números válidos.")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora Simple")

# Crear variables para los resultados
resultado_suma = tk.StringVar()
resultado_resta = tk.StringVar()
resultado_multiplicacion = tk.StringVar()
resultado_division = tk.StringVar()

# Crear etiquetas y entradas para los números
tk.Label(root, text="Número 1:").grid(row=0, column=0)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

tk.Label(root, text="Número 2:").grid(row=1, column=0)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

# Botón para calcular
calcular_btn = tk.Button(root, text="Calcular", command=calcular)
calcular_btn.grid(row=2, column=0, columnspan=2)

# Etiquetas para mostrar los resultados
tk.Label(root, textvariable=resultado_suma).grid(row=3, column=0, columnspan=2)
tk.Label(root, textvariable=resultado_resta).grid(row=4, column=0, columnspan=2)
tk.Label(root, textvariable=resultado_multiplicacion).grid(row=5, column=0, columnspan=2)
tk.Label(root, textvariable=resultado_division).grid(row=6, column=0, columnspan=2)

# Ejecutar la aplicación
root.mainloop()

