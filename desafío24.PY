"""Desafío 24
Desarrollar un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y 
múltiplos de 10. Nota: para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea 
divisible por 400."""

año = int(input("Ingrese un año: "))
año1 = int(input("Ingrese otro año: "))

print(f"Los años bisiestos y múltiplos de 10 entre el {año} y el {año1} son los siguientes: ")

for años in range(año, año1):
   if años % 4 == 0 and años % 100 == 0 and años % 400 == 0 or años % 10 == 0 or años % 4 == 0 and años % 100 != 0:
    print(años)

