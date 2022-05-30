# una vez instalado el sqlite, importo la libreria que maneja la BBDD. #en realidad no hace falta instalarlo.
#from asyncio.windows_events import NULL
import sqlite3 as sq3

con = sq3.connect("mi_bbdd.db") #conexión a la BBDD, como argumento paso el nombre del archivo.
cur = con.cursor() #con estas cosas ya puedo tener mi BBDD.

instruct1 = '''CREATE TABLE IF NOT EXISTS escuelas (
  _id INTEGER PRIMARY KEY AUTOINCREMENT,  
  nombre varchar(45) DEFAULT NULL,
  localidad varchar(45) DEFAULT NULL,
  provincia varchar(45) DEFAULT NULL,
  capacidad INTEGER DEFAULT NULL)'''

instruct2 = '''CREATE TABLE  IF NOT EXISTS alumnos (
  _id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_escuela INTEGER DEFAULT NULL,
  legajo INTEGER DEFAULT NULL,
  nombre varchar(45) DEFAULT NULL,
  nota decimal(10,0) DEFAULT NULL,
  grado INTEGER DEFAULT NULL,
  email varchar(45) NOT NULL,
  FOREIGN KEY (id_escuela) REFERENCES escuelas(id))'''

cur.execute(instruct1)
cur.execute(instruct2)

lista1 = [(1,'Normal 1','Quilmes','Buenos Aires',250),(2,'Gral. San Martín','San Salvador','Jujuy',100),(3,'Belgrano','Belgrano','Córdoba',150),(4,'EET Nro 2','Avellaneda','Buenos Aires',500),(5,'Esc. N° 2 Tomás Santa coloma','Capital Federal','Buenos Aires',250)]

lista2 = [(1,2,1000,'Ramón Mesa',8,1,'rmesa@mail.com'),(2,2,1002,'Tomás Smith',8,1,''),(4,1,101,'Juan Perez',10,3,''),(5,1,105,'Pedro González',9,3,''),(6,5,190,'Roberto Luis Sánchez',8,3,'robertoluissanchez@gmail.com'),(7,2,106,'Martín Bossio',8,3,''),(8,4,100,'Paula Remmi',3,1,'mail@mail.com'),(9,4,1234,'Pedro Gómez',6,2,'')]

'''
cur.executemany('INSERT INTO escuelas VALUES (?,?,?,?,?)', lista1)
cur.executemany('INSERT INTO alumnos VALUES (?,?,?,?,?,?,?)', lista2)
'''
query1 = '''SELECT alumnos.legajo, alumnos.nombre, alumnos.nota, alumnos.email, escuelas.nombre, escuelas.localidad, escuelas.provincia FROM alumnos
INNER JOIN escuelas ON alumnos.id_escuela = escuelas._id'''

for registro in cur.execute(query1):
    print(registro)

con.commit() #Ejecuta cambios en la BBDD
con.close()
