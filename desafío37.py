""" Desafío 37
Una Chocolateria tiene a la venta bombones en cajas de 5, 8 y 13 unidades. Desarrollar una función que reciba el dato de la cantidad
de bombones pedida por el cliente, luego, calcule si es posible o no armar una entrega con esa cantidad pedida."""

caja1 = 5
caja2 = 8
caja3 = 13
pedido = []

cantidad = int(input("Ingresa la cantidad de bombones que desea ordenar: "))      

if cantidad % 13 == 0 & cantidad // 8 == 0 & cantidad // 5 == 0: 
    pedido.append(cantidad//13) 
    print("El pedido que realizo pueden ser ",*pedido," cajas de ",caja3," de bombones c/u.")
 
if cantidad % 8 == 0 & cantidad // 13 == 0 & cantidad // 5 == 0:
    pedido.append(cantidad//8) 
    print("El pedido que realizo pueden ser ",*pedido," cajas de ",caja2," de bombones c/u.")
      
if cantidad % 5 == 0 & cantidad // 8 == 0 & cantidad // 13 == 0:
    pedido.append(cantidad//5) 
    print("El pedido que realizo pueden ser ",*pedido," cajas de ",caja1," de bombones c/u.")
    
else:
    print("No es posible armar una entrega con esa cantidad pedida.")