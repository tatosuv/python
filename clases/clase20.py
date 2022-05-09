#Función promedio

'''
def promediar(n): #si yo quiero promediar 3 numeros, n va a ser 3
    subtotal = 0
    for i in range(n):
        subtotal += int(input("Ingrese cifra: "))
    promedio = subtotal / n
    return promedio

nro = int(input("Cuantos numeros quiere promediar?: "))
print(promediar(nro))
'''
#Función contar
'''
def contar(a, b):
    for i in range (a, b+1):
        print(i)

desde = int(input("Desde que nro?: "))
hasta = int(input("Hasta que nro?: "))
contar(desde, hasta)
'''

#Valores por defect

#valores que va a recibir la funcion para reemplazar si falta alguno
'''
def contar(a=90, b=100):
    for i in range (a, b+1):
        print(i)

contar(80)
'''

#Parametros y argumentos
'''
def sumar(a,b): # ---> parámetros (valores todavía desconocídos)

sumar(10, 5) # ---> argumentos
'''

# Parámetros indefinidos

'''
def sumar(*args): #Esto me va a crear una tupla con los argumentos que recibe
    sumatoria = 0
    for i in args:
        sumatoria += i
    print(sumatoria)

sumar()
sumar(2,4)
sumar(4,8,10)
sumar(4,8,10,22,4,6,44,33,27)
'''
'''
def promediar(*args):
    cantidad = len(args)
    subtotal = 0
    for i in args:
        subtotal += i
    promedio = subtotal/cantidad
    print(promedio)

promediar(8.5, 9.45)
'''

# Ambitos y alcances
# en py las variables que se utilizan pertenecen a un ambito particular(decimos que tienen un alcance o scope) que puede ser local o global
'''
nro = 10

def locales():
    global nro
    nro = 25
    print(nro)

print(nro)
locales()
print(nro)
'''

# Métodos
#Un método es una función definida dentro de una clase

mensaje = "mensaje de bienvenida"
longi = len(mensaje)
print(longi)

nombre = "jUANA"
print(nombre.swapcase())