import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Servicio:
    def __init__(self, nombre, tarifa):
        self.nombre = nombre
        self.tarifa = tarifa
        self.consumo = 0

    def calcular_costo(self):
        return self.consumo * self.tarifa

class CalculadoraServicios:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Servicios")

        # Estilos personalizados
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12), padding=5, background="lightgrey", foreground="darkblue")
        style.configure("TButton", font=("Helvetica", 12), padding=5, background="lightblue", foreground="black")
        style.map("TButton", background=[('active', 'blue')])
        style.configure("TEntry", font=("Helvetica", 12), padding=5, foreground="black")

        # Configurar el canvas y la imagen de fondo
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack(fill="both", expand=True)

        self.bg_image = Image.open()  # Cambia "background.jpg" por el nombre de tu imagen
        self.bg_image = self.bg_image.resize((600, 400), Image.ANTIALIAS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Crear servicios
        self.servicios = {
            'agua': Servicio('Agua', 0.50),
            'luz': Servicio('Luz', 0.30),
            'gas': Servicio('Gas', 0.45)
        }

        self.crear_interfaz()

    def crear_interfaz(self):
        self.consumos = {}
        row = 0

        for nombre, servicio in self.servicios.items():
            label = ttk.Label(self.root, text=f"Consumo de {servicio.nombre} (m³/kWh):", style="TLabel")
            self.canvas.create_window(50, 50 + row * 50, anchor="nw", window=label)
            
            consumo_var = tk.DoubleVar()
            entry = ttk.Entry(self.root, textvariable=consumo_var, style="TEntry")
            self.canvas.create_window(300, 50 + row * 50, anchor="nw", window=entry)

            self.consumos[nombre] = consumo_var
            row += 1

        calcular_btn = ttk.Button(self.root, text="Calcular", command=self.calcular_total, style="TButton")
        self.canvas.create_window(200, 200, anchor="nw", window=calcular_btn)

        self.resultado_lbl = ttk.Label(self.root, text="Costo total: $0.00", font=("Helvetica", 14, "bold"), background="lightgrey", foreground="red")
        self.canvas.create_window(150, 250, anchor="nw", window=self.resultado_lbl)

    def calcular_total(self):
        total = 0
        for nombre, servicio in self.servicios.items():
            servicio.consumo = self.consumos[nombre].get()
            total += servicio.calcular_costo()

        self.resultado_lbl.config(text=f"Costo total: ${total:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraServicios(root)
    root.mainloop()