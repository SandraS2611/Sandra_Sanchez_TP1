"""Desafío 1
Solicitar al usuario que ingrese su número de cliente. Si el número es el 100, imprimir
"Ganaste un premio".

numero_ingresado = int(input("Ingrese el número de cliente: "))

if numero_ingresado == 100:
  print("Ganaste un premio")
else:
  print("Probá de nuevo.")
"""
  
# WHILE
numero_ingresado = 0

while numero_ingresado != 100:
  numero_ingresado = int(input("Ingrese el número de cliente: "))

  if numero_ingresado == 100:
    print("Ganaste un premio.")
  else:
    print("Probá de nuevo. \n")
    