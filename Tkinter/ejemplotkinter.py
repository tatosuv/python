from tkinter import *

raiz = Tk()
raiz.title('GUI - Com 22040')

#Barra Menú
barramenu = Menu(raiz) #Menu pertenece a la libreria de Tkinter, dentro le informo donde va a estar, le digo qu eva a estar en mi raiz.
raiz.config(menu=barramenu)

bbddmenu = Menu(barramenu, tearoff=0)
bbddmenu.add_command(label='Conectar')
bbddmenu.add_command(label='Salir')

barramenu.add_cascade(label='BBDD', menu=bbddmenu)



raiz.mainloop() #nuestra ultima linea tiene que ser el mainloop, mantiene abierta nuestra interfaz gráfica hasta que alguien la cierre.