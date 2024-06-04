""" Desafío 14
Solicitar al usuario que ingrese un número entero positivo e imprimir todos los números correlativos entre el ingresado por el usuario y 
uno menos del doble del mismo."""

n = int(input("Ingrese un nro positivo: "))

for n in range(n + 1, ((2 * n)+1) - 1):
 print(n)