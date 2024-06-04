"""Desafío 8
Desarrollar un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”. 
Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un String de más de un carácter, informarle 
que no se puede procesar el dato."""

letra = input("Ingrese una letra: ").lower()
vocales = "aeiou"

if letra in vocales:
    print("Es una vocal")
else:
    print("No se puede procesar el dato.")