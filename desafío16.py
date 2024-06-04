vocales = "aeiou"
lista_vocales = []
frase = input("Ingrese una frase: ")
for i in vocales:
 if i in frase:
     lista_vocales.append(i)
print(f"Las vocales que aparecen en la frase '{frase}' son : {lista_vocales}" )
    
