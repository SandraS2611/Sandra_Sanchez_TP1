frase = [input("Ingrese una frase: ").upper()]
vocales = "aeiou"

for i in frase:
    if i in vocales:
        suma = suma + vocales
        print(suma)


