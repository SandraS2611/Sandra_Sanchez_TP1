'''1) MOSTRAR LA SUMA DE LOS NÚMEROS MÚLTIPLOS DE 5 MEORES A 50.''' 
'''2) DEL EJERCICIO ANTERIOR, SOLICITAR EL NÚMERO LIMITE A CALULAR'''

'''SUMAR MULTIPLOS DE 5'''

'''MI SOLUCIÓN'''
numero = 0
suma = 0

while numero < 50:
    suma = suma + numero
    numero += 5
print(f"La suma de los números menores a 50 y múltiplos de 5 es {suma}")  
    
    
'''SOLUCIÓN 1 - COMPLETO'''
contador = 0
suma = 0

numero_maximo = int(input("Introduce el número máximo: "))

while contador < numero_maximo:
    suma += contador #OPERADOR DE ASIGNACIÓN
    contador += 5
print("La suma es ",suma)
