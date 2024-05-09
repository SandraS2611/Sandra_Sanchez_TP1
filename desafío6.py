nom1 = input("Ingrese el primer nombre: ").upper()
nom2 = input("Ingrese el segundo nombre: ").upper()

if (nom1[0] == nom2[0]) or (nom1[-1] == nom2[-1]):
   print("Coincidencia")
else:
  print("No hay coincidencia")


  #str1[len(str1)-1] == str2[len(str2)-1] //PRACTICAR