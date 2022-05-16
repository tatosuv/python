'''
m1 = [1,2,3,4,5]
m2= ["hola","chau", True]

#extend # concatena 2 listas --> suma los elementos al final, tantos como haya en la lista.

m1.extend(m2)
print(m1)

#append #agrega la lista como un unico elemento = append agrega un elemento al final

#m1.append(m2)

'''
#DATETIME

import datetime as dtm

t = dtm.time(20,30,29,5)
print(t)
print(f'{t.hour} horas')
print(f'{t.minute} minutos')
print(f'{t.second} segundos')
print(f'{t.microsecond} microsegundos')
print(f'Son las {t.hour} horas y {t.minute} minutos')

#fechas

today = dtm.date.today()

print(today)
print(f'Fecha actual: {today.ctime()}')

tt = today.timetuple()
print(f'Año: {tt.tm_year}')
print(f'Mes: {tt.tm_mon}')
print(f'Día: {tt.tm_mday}')
print(f'Hora: {tt.tm_hour}')
print(f'Día: {tt.tm_wday}')
print(f'Día del año: {tt.tm_yday}')
print(tt)
# --------------------------------------
print(f'Ordinal: {today.toordinal()}')
print(f'Año: {today.year}')
print(f'Mes: {today.month}')
print(f'Día: {today.day}')


from datetime import date, datetime, timedelta

my_time = datetime.now() # te imprime la hora exacta en el momento
print(my_time)

my_day = date.today()
prox_semana = my_day + timedelta(days=7)
print(prox_semana)