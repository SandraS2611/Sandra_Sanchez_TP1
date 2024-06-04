cantidad = int(input("Ingresa la cantidad de años que quiere determinar si son bisiesto o no: "))
for i in range(1,cantidad + 1):
    año = int(input(f"Ingrese el {i}° año: "))
    if año % 4 == 0 & año % 100 == 0 & año % 400 == 0:
        print(f"{año} es un año bisisesto.")
    else:
        print(f"{año} no es un año bisisesto.") 