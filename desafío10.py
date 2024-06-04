"""Desafío 10
Un instituto de enseñanza de inglés necesita un programa que le permita, cada día, procesar observaciones sobre las clases de ese día. 
El instituto dicta clases a estudiantes de distintos niveles y cada nivel tiene clases en un día de la semana diferente: los lunes se 
dicta el nivel inicial, los martes el nivel intermedio, los miércoles el nivel avanzado, los jueves son para práctica hablada y los 
viernes se dicta inglés para viajeros. Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato "día, DD/MM", 
donde [día] es un día de la semana, DD es el número de día y MM es el número de mes. Si el usuario ingresa un día de la semana inexistente
o una fecha cuyo día supere el número 31 o el mes supere el número 12, finalizar el programa indicando que se produjo un error. 
Debe permitirse que ingrese el día de la semana en minúsculas o mayúsculas indistintamente. Como precondición se tiene que lo ingresado
por el usuario tendrá la forma <[alfanumérico], [numérico]/[numérico]>. Una vez indicada la fecha, el usuario necesita poder indicar si 
ese día se tomaron exámenes, pero eso sólo si se trata de los niveles inicial, intermedio o avanzado, ya que las prácticas habladas y el 
inglés para viajeros no tienen exámenes. Si hubo exámenes, el usuario ingresará cuántos alumnos aprobaron y cuántos no, y el programa le 
mostrará el porcentaje de aprobados. Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el porcentaje de 
asistencia a clase y el programa le indicará "asistió la mayoría" en caso de que la asistencia sea mayor al 50% o "no asistió la mayoría" 
si no es así. Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del mes 7, se deberá imprimir 
"Comienzo de nuevo ciclo" y solicitar al usuario que ingrese la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, 
para luego imprimir el ingreso total en $."""

fecha = int(input("Ingrese una fecha (DD/MM): "))
dia = int(fecha / 100) 
mes = int(fecha % 100) 

while (dia == 0) | (dia > 31):
    print("Dia no válido")
    break

while (mes == 0) | (mes > 12):
    print("Mes no válido")
    break

print(f"{dia}/{mes}")


dia_semana = input("Ingrese el día de la semana que desea consultar: ").lower()

if dia_semana == "lunes":
  print("Este día tuvo clases el Nivel Inicial y se tomó examen.")
  aprobados = []
  desaprobados = []
  alumnos = int(input(f"Ingrese la cantidad de alumnos que rindieron: "))
  for i in range(1, alumnos + 1):
    nota = int(input(f"Ingresa la nota del {i}° alumno: "))
    if nota <= 5:
      if nota not in desaprobados:
        desaprobados.append(nota)
        i = i - 1
    if nota >= 6:
      if nota not in aprobados:
        aprobados.append(nota)
        i = i - 1
  print(f"El promedio de alumnos aprobados es del {round((len(aprobados)/alumnos)*100)}%.")

if dia_semana == "martes":
  print("Este día tuvo clases el Nivel Intermedio y se tomó examen.")
  aprobados = []
  desaprobados = []
  alumnos = int(input(f"Ingrese la cantidad de alumnos que rindieron: "))
  for i in range(1, alumnos + 1):
    nota = int(input(f"Ingresa la nota del {i}° alumno: "))
    if nota <= 5:
      if nota not in desaprobados:
        desaprobados.append(nota)
        i = i - 1
    if nota >= 6:
      if nota not in aprobados:
        aprobados.append(nota)
        i = i - 1
  print(f"El promedio de alumnos aprobados es del {round((len(aprobados)/alumnos)*100)}%.")

if dia_semana == "miercoles":
  print("Este día tuvo clases el Nivel Avanzado y se tomó examen.")  
  aprobados = []
  desaprobados = []
  alumnos = int(input(f"Ingrese la cantidad de alumnos que rindieron: "))
  for i in range(1, alumnos + 1):
    nota = int(input(f"Ingresa la nota del {i}° alumno: "))
    if nota <= 5:
      if nota not in desaprobados:
        desaprobados.append(nota)
        i = i - 1
    if nota >= 6:
      if nota not in aprobados:
        aprobados.append(nota)
        i = i - 1
  print(f"El promedio de alumnos aprobados es del {round((len(aprobados)/alumnos)*100)}%.")
  
if dia_semana == "jueves":
  print("Este día se dictó práctica hablada.")
  total_inscriptos = int(input("Ingrese el total de alumnos inscriptos a las prácticas: "))
  asistencia = int(input("Ingrese la cantidad de alumnos que asistieron: "))
  if asistencia > total_inscriptos/2:
    print("Asistió la mayoría.")
  else:
    print("No asistió la mayoría.")   
  
if dia_semana == "viernes":
  if dia == 1 & mes == 1 | dia == 1 & mes == 7:
    print("Este día se dictó Inglés para Viajeros.")  
  aranceles = []
  print("Comienzo de nuevo ciclo")
  cantidad_alumnos = int(input(f"Ingrese la cantidad de alumnos que se inscribieron: "))
  for i in range(1, cantidad_alumnos + 1):
    pago = int(input(f"Ingrese cuanto abonó el {i}° alumno: $ "))
    aranceles.append(pago)
    i = i + 1
     
  print(f"El ingreso total es $ {sum(aranceles)}.")
   
if dia != dia_semana:
  print("error")