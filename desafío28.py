""" Desafío 28
Encriptar un mensaje utilizando el método de “la cifra del césar”, que consiste en correr cada letra del mensaje –considerando la posición
de cada una en el alfabeto– una determinada cantidad de lugares. Ejemplo: si el corrimiento es de 2 lugares, la palabra “HOLA” se 
transforma en “JQNC”. Si el alfabeto termina antes de poder correr la cantidad de lugares necesarios, se vuelve a comenzar desde la letra “a”."""

abecedario = "abcdefghijklmnñopqrstuvwxyz"
msj = ""
msjencriptado =""

corrimiento = int(input("Ingresa la cantidad de veces que se correrán: "))
msj = input("Ingresa un mensaje: ")
for letra in msj.lower():
    if letra in abecedario:
        encript = abecedario.find(letra)
        encript += corrimiento
        if encript >= 27:
            encript -= 27
        msjencriptado += abecedario[encript]
else:
    msjencriptado += letra
    print("El mensaje encriptado es: ",msjencriptado)