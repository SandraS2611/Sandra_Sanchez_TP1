"""Desafío 16
Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas)."""

frase = input("Ingresa una frase: ")
vocales ="aeiou"

for i in vocales:
 if i in frase:    
  print(i) 