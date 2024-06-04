"""Desafío 26
Desarrolle una función para invertir un dato alfanumérico. Pruebe si el código funciona correctamente."""

def invertir(dato):
    if len(dato) == 0:
        return dato
    else:
        return invertir(dato[1:]) + dato[0]
    
dato = input("Ingresar dato alfanumérico: ")
print(invertir(dato))
