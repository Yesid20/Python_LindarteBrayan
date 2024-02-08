## ----------------------------------
# ---- Ejercicio Json ----
## ----------------------------------

import json

with open("data.json") as f:
    data = json.load(f)

nombres_comerciales = set()
for comercial in data["ventas"]["comerciales"]:
    if "apellido1" in comercial and comercial["apellido1"] == "Ruiz":
        nombres_comerciales.add(comercial["nombre"])
    elif "apellido2" in comercial and comercial["apellido2"] == "Ruiz":
        nombres_comerciales.add(comercial["nombre"])

for nombre in sorted(nombres_comerciales):
    print(nombre)