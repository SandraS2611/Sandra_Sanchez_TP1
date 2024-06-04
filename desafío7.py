""" Desafío 7
Desarrollar un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido 
rojo, candidato B por el partido verde, candidato C por el partido azul. Según el candidato elegido (A, B ó C) se le debe imprimir 
el mensaje “Usted ha votado por el partido [color que corresponda al candidato elegido]”. Si el usuario ingresa una opción que no 
corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”."""

candidatos = input("Ingrese el nombre del Candidato: ").upper()

if candidatos == "A":
 print("Usted a votado al candidato del Partido Rojo.")

elif candidatos == "B":
 print("Usted a votado al candidato del Partido Verde.") 
 
elif candidatos == "C":
 print("Usted a votado al candidato del Partido Azul.") 

else:
 print("Opción errónea.")