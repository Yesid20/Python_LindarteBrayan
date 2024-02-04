## -------------------------------------------------------------
## ---- Ejercicio Clase ----
## -------------------------------------------------------------
#REALIZAR UN PROGRAMA QUE USE UN DICCIONARIO PARA GESTIONAR LOS PRODUCTOS
#Y PRECIOS DE LA TABLA, DONDE SE LE PREGUNTE AL USUARIO POR UN PRODUCTO
#Y LA CANTIDAD. AL FINALIZAR MOSTRAR EN LA CONSOLA EL PRECIO TOTAL. SI
#EL PRODUCTO NO ESTA DEBE MOSTRAR UN MENSAJE INFORMANDO SOBRE ELLO
print("Welcome to store Martica")
print("Productos en tienda son: ")
productos_tienda = {
'Empanada': "3500",
'Pizza': "2500",
'Sandwich': "2800",
'Gaseosa': "2000",
'Jugo': "1500"
}
print(productos_tienda)
question = input("¿Que producto desea? ")
cantidad = int(input("¿Que cantidad desea? "))
print(f"Escogiste {question} y una cantidad de {cantidad}")
costo = int(productos_tienda[question])
valorTotal = (costo * cantidad)
print(f"Su valor total es de {valorTotal} pesos colombianos")

## Realizo por Brayan Yesid Lindarte anaya - 1010120365
 