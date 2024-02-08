## ----------------------------------
# ---- Ejercicio Json ----
## ----------------------------------

import json 

with open("data.json") as f:
    data = json.load(f)

ids_clientes = set()
for pedido in data["ventas"]["pedidos"]:
    ids_clientes.add(pedido["id_cliente"])
for id_cliente in ids_clientes:
    print(id_cliente)

## Desarrollado por BRAYAN YESID LINDARTE ANAYA - 1010120365