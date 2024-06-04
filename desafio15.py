""" Desafío 15
Desarrollar un programa que solicite al usuario una cantidad y luego itere la cantidad de veces dada. En cada iteración, solicitar al 
usuario que ingrese un número. Al finalizar, mostrar la suma de todos los números ingresados."""

suma = 0
cantidad = int(input(f"Ingresa una cantidad :"))
for i in range(1, cantidad + 1):
  num = int(input(f"Ingresa el {i} número: "))
  suma = suma + num
print(f"La suma de todos los números es = {suma}")


