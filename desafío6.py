name1 = input("Ingrese el primer nombre: ")
name2 = input("Ingrese el segundo nombre: ")

if (name1[0] == name2[0]) or (name1[-1] == name2[-1]):
   print("Coincidencia")
else:
  print("No hay coincidencia")