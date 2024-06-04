""" Desafío 27
Solicitar al usuario que ingrese los nombres de los estudiantes de primer año, finalizando al ingresar “S”. Luego, solicitar al usuario 
que ingrese los nombres de los estudiantes de segundo año, finalizando al ingresar “S”. A continuación informar:  la lista de todos los 
nombres de los estudiantes de primer año y de segundo año, sin repeticiones.  La lista de todos los nombres de los estudiantes de primer 
año y de segundo año que se repiten.  la lista de todos los nombres de los estudiantes de primer año que no se repiten en segundo año."""

alumnos1ro = []
alumnos2do = []
nombresrepetidos = []
nombres = []
while True:
    nombres1ro = input("Ingresa el nombre del alumno de 1re año: ")
    if nombres1ro == "S":
        break    
    if nombres1ro not in alumnos1ro :
        alumnos1ro.append(nombres1ro)           
while True:
    nombres2do = input("Ingresa el nombre del alumno de 2do año: ")
    if nombres2do == "S":
        break    
    if nombres2do not in alumnos2do :
        alumnos2do.append(nombres2do)  
        
print(f"Los alumnos 1ro son: {alumnos1ro}")
print(f"Los alumnos de 2do son: {alumnos2do}")

for nombres1ro in alumnos1ro:
    if nombres1ro in alumnos2do:
        nombresrepetidos.append(nombres1ro)
print(f"Los nombres que se repiten es/son: {nombresrepetidos}")

for nombres1ro in alumnos1ro:
    if nombres1ro not in alumnos2do:
        for nombres2do in alumnos2do:
            if nombres2do not in alumnos1ro:
                nombres.append(nombres1ro+" , "+nombres2do)
print(f"Los nombres que no se repiten son: {nombres}")

         
      