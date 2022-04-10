#ROTACION DE GUARDIAS EN FORMA DE CALENDARIO

print( "Cuestionario Inicial" )
#Insertar el NOMBRE DE LA EMPRESA que se deben guardar en una memoria
mainname = input ( "Nombre de la Empresa: " )

#Insertar NUMERO y NOMBRES de las personas a rotar
#NOTA: Debe ser en el orden de la rotacion preferencial, es decir, nombre1 es la persona asignada al 01/01
N = int ( input ( "¿Cuántas personas participarán en la rotación?:   " ) )
print ( "Indique los nombres de los participantes en el orden deseado.")
print ( "Recuerde que la primera persona debe coincidir con el 01 de Enero" )

names = [ ]
i = 0
for i in range ( N ):
    names.append ( input (f"Nombre {i+1}: " ) )


#Insertar la posibilidad de un SALTO ANUAL en la rotacion y la FECHA (DIA Y MES)
jump = str ( input ( "¿Desea que se realiza un salto en la rotación para un cambio en la misma?: " ) )
if jump ==  "SI" :
    print("NOTA: El mes debe colocarlo en el rango de 1-12 y el día en el rango 1-31")
    month_jump = input ( "Inserte el mes en el que desea realizar el cambio de rotación: " )
    day_jump = input ( "Inserte el día en el que desea realizar el cambio de rotación: " )
elif jump == "NO" :
    month_jump = 0
    day_jump = 0
else:
    print ("error")

#Informacion tipo calendario
import sys 
import datetime as dt 
import calendar 

rotador = dt.timedelta(days=N)

#Rotacion 
w_year = int(input("Inserte el Año de la rotación deseada: "))  #año deseado
w_month = int(input("Inserte el Mes de la rotación deseada: "))  #mes deseado

rotacion = []
i = 0
month = 1
current_month = []
year_rotations = []


isLeapYear = (w_year % 4 == 0)
firstday = dt.date(w_year,1,1)
delta = lambda i: dt.timedelta(days=i)
daysInCurrentYear = (365,366)[isLeapYear]
days_year = [firstday + delta(i) for i in range(daysInCurrentYear)]
rotacion = names*366


for (currentDate,person) in zip(days_year,rotacion):
    if month != currentDate.month:
        year_rotations += [current_month]
        current_month = []
        month = currentDate.month
    current_month += [person]


#SALIDA 1: Rotacion del AÑO ACTUAL (Predeterminado)

#SALIDA 2: Rotacion AÑO Y MES ESPECÍFICO

esp = w_month-1
second = dt.date (w_year, w_month,1)

if (w_month == 1) or (w_month == 3) or (w_month == 5) or (w_month == 7) or (w_month == 8) or (w_month == 10) or (w_month == 12):
    days_month = [second + delta(i) for i in range(31)]
elif (w_month == 4)  or (w_month == 6) or (w_month == 9) or (w_month == 11):
    days_month = [second + delta(i) for i in range(30)]
elif (w_month == 2) and (w_year % 4 == 0):
    days_month = [second + delta(i) for i in range(29)]
else:
    days_month = [second+ delta(i) for i in range(28)]

if w_month == 1 : mes = "ENERO"
elif w_month == 2: mes = "FEBRERO"
elif w_month == 3: mes = "MARZO"
elif w_month == 4: mes = "ABRIL"
elif w_month == 5: mes = "MAYO"
elif w_month == 2: mes = "JUNIO"
elif w_month == 2: mes = "JULIO"
elif w_month == 2: mes = "AGOSTO"
elif w_month == 2: mes = "SEPTIEMBRE"
elif w_month == 2: mes = "OCTUBRE"
elif w_month == 2: mes = "NOVIEMBRE"
else: mes = "DICIEMBRE"

print("La rotación de", mainname, "en el mes de", mes)
print (list(zip (days_month, year_rotations[esp])))
