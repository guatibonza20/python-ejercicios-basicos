from tkinter import* 
class app():
    def __init__(self):

        ventana=Tk()
        ventana.title("ventana principal")
        ventana.geometry("500x500")
        ventana.config(bg="red")

        self.text1=Entry(ventana,bg="red")
        self.text1.place(x=100,y=30)
        self.label1=Label(ventana, text="nombre")
        self.label1.place(x=20,y=30)
        self.label2=Label(ventana, text="apellido")
        self.label2.place(x=80,y=80)
        self.text2=Entry(ventana,bg="red")
        self.text2.place(x=200,y=80)




        ventana.mainloop()


Objeto_Ventana=app()


