from ast import Str
from tkinter import *
from tkinter import messagebox


'''
===========================================================
                    FUNCIONALIDAD
===========================================================
'''
#Menu
#Menu BBDD
#mMenú Limpiar
#Menú Ayuda
# Licencia
def licencia():
    # CREATIVE COMMONS GNU GPL https://www.gnu.org/licenses/gpl-3.0.txt
    gnuglp = '''
    Demo de un sistema CRUD en Python para gestión 
    de alumnos
    Copyright (C) 2022 - Lisandro "El crack" Suvercase
    Email: lisandro@suvercase.com\n=======================================
    This program is free software: you can redistribute it 
    and/or modify it under the terms of the GNU General Public 
    License as published by the Free Software Foundation, 
    either version 3 of the License, or (at your option) any 
    later version.
    This program is distributed in the hope that it will be 
    useful, but WITHOUT ANY WARRANTY; without even the 
    implied warranty of MERCHANTABILITY or FITNESS FOR A 
    PARTICULAR PURPOSE.  See the GNU General Public License 
    for more details.
    You should have received a copy of the GNU General Public 
    License along with this program.  
    If not, see <https://www.gnu.org/licenses/>.'''
    messagebox.showinfo("LICENCIA", gnuglp)
    
# ACERCA DE

def acerca():
    messagebox.showinfo("ACERCA DE....", "Creado por Lisandro Suvercase \npara Codo a Codo 4.0 - Big Data\n Mayo 2022\nEmail: blabla@hola.com")
'''
===========================================================
                    INTERFAZ GRÁFICA
===========================================================
'''


raiz = Tk()
raiz.title('GUI - Com 22040')

#Barra Menú
barramenu = Menu(raiz) #Menu pertenece a la libreria de Tkinter, dentro le informo donde va a estar, le digo qu eva a estar en mi raiz. #Creo la barra menu
raiz.config(menu=barramenu) #agrega el menú a la ventana principal

bbddmenu = Menu(barramenu, tearoff=0) #Crea submenú BBDD
bbddmenu.add_command(label='Conectar') #Agrega un botón al submenú BBDD
bbddmenu.add_command(label='Salir') #Agrega un botón al submenú BBDD

limpiarmenu = Menu(barramenu,tearoff=0)
limpiarmenu.add_command(label='Limpiar campos')


ayudamenu = Menu(barramenu,tearoff=0)
ayudamenu.add_command(label="Licencia", command=licencia)
ayudamenu.add_command(label="Acerca de...", command=acerca)


barramenu.add_cascade(label='BBDD', menu=bbddmenu)# Crea el botón BBDD y le asigna el submenú
barramenu.add_cascade(label='Limpiar', menu=limpiarmenu)
barramenu.add_cascade(label='Acerca de', menu=ayudamenu)



# FRAMECAMPOS

framecampos = Frame(raiz) #framecampos es el nombre que yo le puse, le puedo poner cualquier nombre, le asigno un objeto (importado de Tkinter) llamado Frame y le digo que va a estar situado en la raiz
framecampos.pack() #el método pack es una forma de acomodar las cosas en una ventana

legajo = StringVar()
alumno = StringVar()
email = StringVar()
calificacion = DoubleVar()
escuela = StringVar()
localidad = StringVar()
provincia = StringVar()

'''
entero = IntVar() #Declara variable de tipo entero
flotante = DoubleVar() #Declara variable de tipo float
cadena = StringVar() #Declara variable del tipo cadena
booleano = BooleanVar() #Declara variable del tipo booleano
'''

legajo_input = Entry(framecampos, textvariable=legajo)
legajo_input.grid(row=0, column=2, padx=10, pady= 10)

alumno_input = Entry(framecampos, textvariable=alumno)
alumno_input.grid(row=1, column=2, padx=10, pady= 10)

email_input = Entry(framecampos, textvariable=email)
email_input.grid(row=2, column=2, padx=10, pady= 10)

calificacion_input =Entry(framecampos, textvariable="Calificacion")
calificacion_input.grid(row=3, column=2, padx=10, pady= 10)

escuela_input = Entry(framecampos, textvariable="Escuela")
escuela_input.grid(row=4, column=2, padx=10, pady= 10)

localidad_input = Entry(framecampos, textvariable="Localidad")
localidad_input.grid(row=5, column=2, padx=10, pady= 10)

provincia_input = Entry(framecampos, textvariable="Provincia")
provincia_input.grid(row=6, column=2, padx=10, pady= 10)

# labels

legajo_label = Label(framecampos,text='Legajo')
legajo_label.grid(row=0, column=1, padx=10, pady=10, sticky='e')

alumno_label = Label(framecampos,text='Alumno')
alumno_label.grid(row=1, column=1, padx=10, pady=10, sticky='e')

email_label = Label(framecampos, text="Email")
email_label.grid(row=2, column=1, padx=10, pady=10, sticky='e')

calificacion_label = Label(framecampos, text="Calificación")
calificacion_label.grid(row=3, column=1, padx=10, pady=10, sticky='e')

escuela_label = Label(framecampos, text="Escuela")
escuela_label.grid(row=4, column=1, padx=10, pady=10, sticky='e')

localidad_label = Label(framecampos, text="Localidad")
localidad_label.grid(row=5, column=1, padx=10, pady=10, sticky='e')

provincia_label = Label(framecampos, text="Provincia")
provincia_label.grid(row=6, column=1, padx=10, pady=10, sticky='e')


#FRAME BOTONERA ----> CRUD(Create, Read, Update, Delete)

framebotones = Frame(raiz)
framebotones.pack()

#CREAR
boton_crear = Button(framebotones, text="Crear")
boton_crear.grid(row=0, column=0, padx=5, pady=10)
#LEER (buscar x nro de legajo)
boton_leer = Button(framebotones, text="Leer")
boton_leer.grid(row=0, column=1, padx=5, pady=10)
#ACTUALIZAR
boton_actualizar = Button(framebotones, text="Actualizar")
boton_actualizar.grid(row=0, column=2, padx=5, pady=10)
#BORRAR
boton_borrar = Button(framebotones, text="Borrar")
boton_borrar.grid(row=0, column=3, padx=5, pady=10)

#FRAME DEL PIE
framecopy = Frame(raiz)
framecopy.pack()

copy_label = Label(framecopy, text='(2022) por Lisandro Suvercase para CaC 4.0 - Big Data')
copy_label.grid(row=0, column=0, padx=10, pady=10)


raiz.mainloop() #nuestra ultima linea tiene que ser el mainloop, mantiene abierta nuestra interfaz gráfica hasta que alguien la cierre.