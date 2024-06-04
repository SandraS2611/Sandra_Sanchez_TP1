"""Desafío 25
Dada una lista no vacía de numeros enteros, cada numero aparece dos veces, excepto uno de ellos. El algoritmo debe encontrar cual de 
ellos no se repite."""

num = [1, 2, 3, 4, 5, 1, 2, 3, 4]

repetidos = []
unico = []

for i in range(len(num)):
  for j in range(len(num)):
    if i != j:
      if num[i] == num[j] and num[i] not in repetidos:
        repetidos.append(num[i])

for n in num:
  if n not in repetidos and n not in unico:
    unico.append(n)
else:
  num.remove(n)  

print(f"El número que no se repite es : {unico}.")

