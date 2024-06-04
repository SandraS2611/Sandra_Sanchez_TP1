""" Desafío 35
 Intercambia los valores de dos variables de tipo entero sin utilizar una tercera variable."""
 
val1 = int(input("Ingresar el 1er valor = "))
val2 = int(input("Ingresar el 2do valor = "))
val1, val2 = val2, val1
print(f"El valor de de la 1er variables es {val1} y de la 2da es {val2}.")
