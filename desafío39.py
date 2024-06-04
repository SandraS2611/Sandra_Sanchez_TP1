""" Desafío 39
Desarrollar un algoritmo en donde se requiera al usuario que ingrese un texto largo y luego a ese mismo dato se le cuenten la cantidad de 
ocurrencias de cada una de las vocales. Tener en cuenta que cada vocal puede presentarse en mayúscula, minúscula o acentuada, de 
tal manera que se obtenga la siguiente información:
 cantidad de ocurrencias de la vocal a: ...
 cantidad de ocurrencias de la vocal e: ...
 cantidad de ocurrencias de la vocal i: ...
 cantidad de ocurrencias de la vocal o: ...
 cantidad de ocurrencias de la vocal u: ...
 cantidad total de vocales: ..."""
 
frase = input("Ingrese una frase ").lower()

vocales=[]
vocal=0
for i in ["a", "e", "i", "o", "u"]:
    vocales.append(frase.count(i))
    vocal += frase.count(i)

print("Vocales a:",vocales[0],", Vocales e:", vocales[1],", Vocales i:",vocales[2],", Vocales o:",vocales[3],", Vocales u:", vocales[4],", Total de Vocales:", vocal)
 