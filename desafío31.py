""" Desafío 31
Dado un numero entero informar la suma de sus dígitos."""

numero = int(input("Ingresa un número "))
num = numero
suma = 0
while num != 0:
 digito = num % 10
 suma += digito
 num = num // 10
print(f"La suma de los dígitos del número {numero} es = {suma} .") 