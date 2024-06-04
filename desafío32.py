"""Desafío 32
Desarrollar la función potencia sin utilizar los operadores de multiplicación o división."""

def multiplicacion(x, y):
    if y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiplicacion(x, y - 1)
    

b=int(input("Ingresa la base "))
e=int(input("Ingresa el exponente "))
potencia=1 
i=0
if b==0 & e==0:
    print("Operación Inválida")
else:
    while i<e:
        potencia=multiplicacion(potencia,b)
        i=i+1
        
print(f"La potencia de {b} elevado a {e} es {potencia} .")
        