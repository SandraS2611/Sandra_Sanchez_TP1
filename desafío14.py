num = int(input("Ingrese un número entero positivo: "))
if num > 0:
    print(f"Todos los números correlativos entre 1 y el doble de {num} que es {num*2} y su anterior que es {(num*2)-1} son: ")
    for i in range(1,(num*2)):
        print(i)
else:
    print("El número no es un entero positivo.")
    
