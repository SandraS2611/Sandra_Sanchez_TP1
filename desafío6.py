""" Desafío 6
Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. A continuación, imprimir 
“coincidencia” si los nombres de ambas personas comienzan con la misma letra ó si terminan con la misma letra. Si no es así, imprimir 
“no hay coincidencia”."""

nom1 = input("Ingrese el primer nombre: ").upper()
nom2 = input("Ingrese el segundo nombre: ").upper()

if (nom1[0] == nom2[0]) or (nom1[-1] == nom2[-1]):
   print("Coincidencia")
else:
  print("No hay coincidencia")


  #str1[len(str1)-1] == str2[len(str2)-1] //PRACTICAR