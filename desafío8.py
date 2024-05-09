letra = input("Ingrese una letra: ").lower()
vocales = "aeiou"

if letra in vocales:
    print("Es una vocal")
else:
    print("No se puede procesar el dato.")