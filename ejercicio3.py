''' MOSTRAR LA SUMA Y LA CANTIDAD DE NÚMEROS PARES COMPRENDIDOS ENTRE 2 NÚMEROS INGRESADOS POR TECLADO '''
''' 5 Y 10 '''
''' 6 '''
''' 8 '''
''' 2 NÚMERO '''

cantidad = 0 # VARIABLE PARA CONTAR LOS NÚMEROS QUE APARECEN

num1 = int(input("Ingrese el 1er número:"))
num2 = int(input("Ingrese el 2do número:"))

while num1 < num2:
    if num1 % 2 == 0: #CONDICIÓN
        print(num1)
        cantidad += 1
    num1 += 1 # ANTES DE TERMINAR EL WHILE SE NECESITA UN CONTADOR 
#TERMINA EL CICLO
print("Hay",cantidad,"números pares")