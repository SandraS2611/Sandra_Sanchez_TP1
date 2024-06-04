""" Desafío 40
Desarrollar un algoritmo en donde se informe el volumen, en litros, de un contenedor de tipo rectangular, redondo o cilíndrico.
Para realizar dichos cálculos se requerirá al usuario que primero seleccione el tipo de contenedor ingresando la opción correspondiente 
y luego se pidan los datos requeridos para el cálculo de ese contenedor en particular. Tips: se sugiere, que se presente un Menú de 
Opciones que luzca de la siguiente forma:
 Menú de Opciones----------------------------------------------------------
1 - Calcular volumen contenedor rectangular
2 - Calcular volumen contenedor redondo
3 - Calcular volumen contenedor cilíndrico
s - Salir"""

while True:
  print("***MENÚ DE OPCIONES***")
  print("1 - Calcular volúmen contenedor rectangular")
  print("2 - Calcular volúmen contenedor redondo")
  print("3 - Calcular volúmen contenedor cilíndrico")
  print("s - Salir")
  opcion = input("Ingresa una opción: ")


  if opcion == "1":
      print("--- INGRESA LAS MEDIDAS DEL CONTENEDOR RECTANGULAR EN CM. ---")
      largo = int(input(f"largo: "))
      alto = int(input(f"alto: "))
      ancho = int(input(f"ancho: "))
      cantidad_litros_rectangulo = (largo*alto*ancho)/1000
      print(f"El volúmen del contenedor rectángular es {round(cantidad_litros_rectangulo)} litros.")
      print("------------------------------------------------------------------------")


  if opcion == "2":
    print("--- INGRESA LAS MEDIDAS DEL CONTENEDOR REDONDO EN CM. ---")
    diametro = int(input(f"Ingresa el diámetro del contenedor redondo: "))
    radio = diametro/2
    cm3 = (radio*radio)**2
    cantidad_litros_circulo = (4*cm3*3.14)/1000
    print(f"El volúmen del contenedor redondo es {round(cantidad_litros_circulo)} litros.")
    print("------------------------------------------------------------------------")


  if opcion == "3":
    print("--- INGRESA LAS MEDIDAS DEL CONTENEDOR CILÍNDRICO EN CM. ---")
    diametro = int(input(f"Ingresa la base del contenedor cilindrico: "))
    altura = int(input(f"Ingresa la altura del contenedor cilindrico: "))
    radio = diametro/2
    cantidad_litros_cilindro = ((3.14*altura)*radio**2)*1000
    print(f"El volúmen del contenedor cilíndrico es {round(cantidad_litros_cilindro)} litros.")
    print("------------------------------------------------------------------------")
    
  elif opcion == "s":
    print(" HASTA LA PRÓXIMA, QUE TENGA UN BUEN DÍA!!! ")
    break
