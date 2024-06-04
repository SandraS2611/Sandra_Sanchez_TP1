vocales = "aeiou"
lista_vocales = []
frase = input("Ingrese una frase: ").lower()
for i in frase:
    if i in vocales:
        lista_vocales.append(i)
        lista_vocales.count(i)        
print(f"La cantidad de vocales en la frase es: {len(lista_vocales)}.")


