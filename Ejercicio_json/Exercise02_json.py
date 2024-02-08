## ----------------------------------
# ---- Ejercicio Json ----
## ----------------------------------

import json 

with open("data.json") as f:
    data = json.load(f)

pedidos_ordenados = sorted(data["ventas"]["pedidos"], key=lambda pedido: pedido["total"], reverse=True)

mayores = pedidos_ordenados[:2]
for pedido in mayores:
    print(f"Pedido ID: {pedido['id']}")
    print(f"Total: {pedido['total']} ")
    print(f"Fecha: {pedido['fecha']}")
    print(f"Id_cliente {pedido['id_cliente']}")
    print(f"Id_comercial {pedido['id_comercial']}")
    print("")

## Desarollado por BRAYAN YESID LINDARTE ANAYA - 1010120365 
