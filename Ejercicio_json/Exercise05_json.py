## ----------------------------------
# ---- Ejercicio Json ----
## ----------------------------------

import json 

with open("data.json") as f:
    data = json.load(f)

comerciales_comision = []
for platica in data["ventas"]["comerciales"]:
    if 0.05 <= platica["comisión"] <= 0.11:
        comerciales_comision.append(platica)

nombres_apellidos = set()
for comercial in comerciales_comision:
    nombres_apellidos.add(f"{comercial['nombre']} {comercial['apellido1']}")
for nombre_apellido in nombres_apellidos:
    print(nombre_apellido)

## Desarrollado por BRAYAN YESID LINDARTE ANAYA - 1010120365 