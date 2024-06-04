"""Desafío 5
Desarrollar un programa que, dado un número entero, muestre su valor absoluto. Nota: para los números positivos su valor absoluto es 
igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado 
por -1 (el valor absoluto de -52 es 52)."""

num = int(input("Ingrese un número Entero: "))
valor_absoluto = num

if num > 0:
 print(str(valor_absoluto))

elif num < 0:
  print(str(valor_absoluto*(-1)))