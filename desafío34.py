"""Desafío 34
Calcular el dato estadístico mediana de una lista dada. Si la lista es de longitud impar, retorna el valor mediana de la misma. 
Si la lista es de longitud par, retorna el promedio de los dos valores mediana. Si la lista está vacía lanzar una excepción ValueError."""

def convertir(lista:list) -> list:
  ret = []
  for i in lista:
    num = int(i)
    ret.append(num)
  
  return ret
    

lista = input("Ingrese una lista de números: ").split(",")
lista = convertir(lista)
lista.sort()
largo = len(lista)
mediana = lista[0]

if(largo%2>0):
    mediana = lista[largo//2]
else:
    num = lista[largo//2]
    num1 = lista[largo//2-1]
    mediana = (num+num1)/2
print("Mediana ",mediana)
