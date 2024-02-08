## ----------------------------------
# ---- Ejercicio Json ----
## ----------------------------------

import json 

with open("data.json") as f:
    data = json.load(f)

pedidos_2017 = []
for pedido in data["ventas"]["pedidos"]:
    if pedido["fecha"].startswith("2017"):
        pedidos_2017.append(pedido)

pedidos_mayores_500 = []
for pedido in pedidos_2017:
    if pedido["total"] > 500:
        pedidos_mayores_500.append(pedido)
for pedido in pedidos_mayores_500:
    print(f"Pedido ID: {pedido['id']}")
    print(f"Fecha: {pedido['fecha']}")
    print(f"Total: {pedido['total']}")
    print("")

## Desarrollado por BRAYAN YESID LINDARTE ANAYA - 1010120365