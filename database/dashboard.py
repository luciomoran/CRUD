"""
Nombre: dashboard.py
Objetivo: Imprime la pantalla principal del CRUD
Autor: Lucio David Morán B
Fecha: 16 de noviembre de 2019
"""

from tkinter import *

def addEmploye():
    #Creamos formulario para ingresar datos del usuario
    agregar = Tk()
    # formulario
    

    agregar.mainloop()




# Programa principal
# Creamos la ventana raiz
raiz = Tk()
raiz.geometry("800x800")

# Creamos menu
menubar = Menu(raiz)

# Creamos primer menu CRUD
filemenu = Menu(menubar, tearoff = 0)

# Definimos opciones del menu crud
filemenu.add_command(label="Agregar", command="addEmploye")
filemenu.add_command(label="Buscar", command="findEmploye")
filemenu.add_command(label="Cambiar", command="changeEmploye")
filemenu.add_command(label="Borrar", command="delEmploye")
menubar.add_cascade(label="Crud", menu=filemenu)

# Creamos  menu Reportes
repmenu = Menu(menubar, tearoff = 0)

# Definimos opciones del menu crud
repmenu.add_command(label="Pantalla", command="listEmploye")
repmenu.add_command(label="PDF", command="pdfEmploye")
menubar.add_cascade(label="Reportes", menu=repmenu)

# Creamos  salir
salirmenu = Menu(menubar, tearoff = 0)

# Definimos opciones del menu crud
salirmenu.add_command(label="Acerca de ...", command="quienesomos")
salirmenu.add_command(label="Salir", command=raiz.quit)
menubar.add_cascade(label="¿Quiénes somos?", menu=repmenu)


raiz.config(menu = menubar)

# ciclo para imprimir menu y esperar selección
raiz.mainloop()