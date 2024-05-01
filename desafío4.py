semana = ["lunes", "martes", "miercoles", "jueves", "viernes"]
fin_de_semana = ["sabado", "domingo"]

dia = input("Ingrese un día de la semana: ").lower()

if dia == "lunes":
  print("Hoy es: " + semana[0])
if dia == "viernes":
  print("Hoy es: " + semana[4] + " y es el último día hábil.")
elif dia not in semana and dia in fin_de_semana:
  print("Es fin de semana.")
elif dia == semana[1] or dia == semana[2] or semana[3]:
  print("Es día laboral.")