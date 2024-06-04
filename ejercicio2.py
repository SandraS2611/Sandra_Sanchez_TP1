''' 1) MOSTRAR LA TABLA DE MULTIPLICAR DEL NÚMERO 7 '''
''' 7 * 1 =7 '''
''' 7 * 2 = 14 '''
''' 2) DEL EJERCICIO ANTERIOR, SOLICITAR EL NÚMERO DE LA TABLA A MULTIPLICAR '''

''' SOLUCIÓN 1 '''
# tabla = 7
# inicio = 1

# while inicio <= 10:
#     resultado = tabla * inicio
#     print(tabla,"*",inicio,"=",resultado)
#     inicio += 1
    
'''SOLUCIÓN 2 '''
tabla = int(input("Ingresa el número de la tabla a consultar: "))
inicio = 1

while inicio <= 10:
    resultado = tabla * inicio
    print(tabla,"*",inicio,"=",resultado)
    inicio += 1