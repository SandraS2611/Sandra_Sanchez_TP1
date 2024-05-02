año = int(input("Ingrese un año: "))

if año % 4 == 0 and año % 100 != 0:
 print("Es un año Bisiesto.")
 
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
    print ("Es un año Bisiesto.")
    
else:
    print("El año ingresado no es Bisiesto.")