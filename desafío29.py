""" Desafío 29
Dada un alfanumérico texto y un caracter x, retornar una lista de enteros representando la distancia mas corta desde cada caracter en 
texto hasta la primer ocurrencia del caracter x."""

texto = []
x = "s"
cadenita = []


texto = input("Ingrese un texto:")
cadenita = texto.find(x)
print(texto[:cadenita])
