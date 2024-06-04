""" Desafío 3
Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. Considerar el caso en que ambos números son iguales."""

nro1 = int(input("Ingrese un número: "))
nro2 = int(input("Ingrese un número: "))

if nro1 > nro2:
 print(f"{nro2} es menor que {nro1}")

elif nro1 < nro2:
 print(f"{nro1} es menor que {nro2}")

else:
 print("Los números son iguales, ambos son: " + str(nro1))