suma = 0
cantidad = int(input(f"Ingresa una cantidad :"))
for i in range(1, cantidad + 1):
  num = int(input(f"Ingresa el {i} número: "))
  suma = suma + num
print(f"La suma de todos los números es = {suma}")


