## ----------------------------------
# ---- Ejercicio Json ----
## ----------------------------------

import json

with open("data.json") as f:
    data = json.load(f)

nombres_clientes = []
for cliente in data["ventas"]["clientes"]:
    nombre = cliente["nombre"].lower()
    if (nombre.startswith("a") and nombre.endswith("n")) or nombre.startswith("p"):
        nombres_clientes.append(cliente["nombre"])

nombres_clientes.sort()

print(", ".join(nombres_clientes))

## Desarrollado por BRAYAN YESID LINDARTE ANAYA - 1010120365 