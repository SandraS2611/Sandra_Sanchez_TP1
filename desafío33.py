""" Desafío 33
Desarrollar una función que reciba como entrada una lista y retorne otra lista con los numeros sumados más uno."""

lista1 = [1,3,5,7,9,11]
lista2 = []

for i in range(len(lista1)):
      lista2.append(lista1[i])

for i in range(len(lista1)):
      lista2[i] = lista2[i] + 1

print(lista2)


