""" Desafío 22
Desarrollar un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos. Al finalizar, mostrar 
la sumatoria de los números negativos y el promedio de los positivos. No olvides que no es posible dividir por cero, por lo que es 
necesario evitar que el programa arroje un error si no se ingresaron números positivos."""

negativos = []
positivos = []
promedio = 0
sumapos = 0
sumaneg = 0

for i in range(1,7):
  num = float(input(f"Ingresa el {i} número: "))
  i += 1
  if num < 0:
    negativos.append(num)
    sumaneg = sumaneg + num
  elif num > 0:
    positivos.append(num)
    sumapos = sumapos + num
    promedio = sumapos / len(positivos)
    
print(f"La suma de los números negativos ingresados es = {sumaneg}") 
print(f"La suma de los números positivos ingresados es = ",promedio)  

