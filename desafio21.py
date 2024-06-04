"""Desafío 21
Desarrollar un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y, 
a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…"""

numero = 60

def fibonacci(numero):
    """Imprimir la Serie Fibonacci hasta un número."""
a,b = 0,1
while a < numero:
    print(a, end="")
    a, b = b, a + b
print()