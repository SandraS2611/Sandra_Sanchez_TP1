"""Desafío 17
Solicitar al usuario que ingrese una frase y luego imprimir la cantidad de vocales que se encuentran en dicha frase."""

frase = input("Ingresa una frase: ")
vocales = "aeiou"
vocal = ""

for x in frase:
    if x in vocales:
        vocal += x
print("Esta cantidad de vocales se encuentran en la frase ingresada:",vocal)