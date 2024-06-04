"""Desafío 36
Desarrollar la función cuadrado_perfecto que reciba un numero entero positivo en una variable de nombre numero. Luego la función debe
retornar la lista de los numeros cuadrados perfectos que no sean numeros pares."""

from math import sqrt

numero = 0
i=1
numero = int(input("Ingresa un número "))

def cuadrado_perfecto():
  cuadrado = []
  if ((int(sqrt(numero))*int(sqrt(numero)))==numero):
      cuadrado.append(numero) 
  return cuadrado
print(cuadrado_perfecto())


  
