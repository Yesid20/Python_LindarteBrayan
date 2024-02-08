## ----------------------------------
# ---- Ejercicio Json ----
## ----------------------------------

import json
from collections import OrderedDict


with open("data.json") as f:
    data = json.load(f)

clientes_sevilla = OrderedDict()
for cliente in data["ventas"]["clientes"]:
    if cliente["ciudad"] == "Sevilla":
        clientes_sevilla[f"{cliente['apellido1']} {cliente['nombre']}"] = {
            "id": cliente["id"],
            "nombre": cliente["nombre"],
            "apellido1": cliente["apellido1"],
        }

clientes_sevilla = OrderedDict(sorted(clientes_sevilla.items()))

for apellido_nombre, cliente in sorted(clientes_sevilla.items()):
    print(f"ID: {cliente['id']}")
    print(f"Nombre: {cliente['nombre']}")
    print(f"Apellido1: {cliente['apellido1']}")
    print("---")

## Desarrollado por BRAYAN YESID LINDARTE ANAYA - 1010120365