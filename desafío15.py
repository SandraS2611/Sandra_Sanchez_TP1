suma = 0
cantidad = int(input("¿Qué cantidad de números desea ingresar? "))
for i in range(1,cantidad + 1):
    num = int(input(f"Ingrese el {i}° número: "))
    suma = suma + num
print(f"La sumatoria de los números ingresados = {suma}")