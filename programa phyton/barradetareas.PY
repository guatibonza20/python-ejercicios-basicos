from tkinter import*

raiz=Tk()

barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)

archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar")
archivoMenu.add_command(label="Salir")


edicionMenu=Menu(barraMenu, tearoff=0)
edicionMenu.add_command(label="copiar")
edicionMenu.add_command(label="cortar")
edicionMenu.add_command(label="pegar")

herramientaMenu=Menu(barraMenu, tearoff=0)
herramientaMenu.add_command(label="Remplazar")


ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="licencia")
ayudaMenu.add_command(label="acerca de")


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="edicion", menu=edicionMenu)
barraMenu.add_cascade(label="herramienta", menu=herramientaMenu)
barraMenu.add_cascade(label="ayuda", menu=ayudaMenu)

raiz.mainloop()

