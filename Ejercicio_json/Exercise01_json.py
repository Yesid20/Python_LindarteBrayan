## ----------------------------------
# ---- Ejercicio Json ----
## ----------------------------------

import json 

with open("data.json") as f:
    data = json.load(f)

pedidos = sorted(data["ventas"]["pedidos"], key=lambda pedido: pedido["fecha"], reverse=True)

for pedido in pedidos:
    print(f"Pedido ID: {pedido['id']}")
    print(f"Fecha: {pedido['fecha']}")
    print("")

## Desarrollado por BRAYAN YESID LINDARTE ANAYA - 1010120365