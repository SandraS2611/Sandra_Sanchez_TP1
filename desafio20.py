""" Desafío 20
Dado un número entero positivo, mostrar su Factorial. El Factorial de un número se obtiene multiplicando todos los números enteros 
positivos que hay entre el 1 y ese número."""

num = int(input("Ingresa un número: "))
factorial = 1

for i in range(1,num+1):
    factorial = i*factorial

print(f"El factorial de {num} es = {factorial}")

