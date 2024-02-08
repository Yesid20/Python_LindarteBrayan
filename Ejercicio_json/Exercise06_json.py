## ----------------------------------
# ---- Ejercicio Json ----
## ----------------------------------

import json

with open("data.json") as f:
    data = json.load(f)

# Crear una lista de todas las comisiones
comisiones = [comercial["comisión"] for comercial in data["ventas"]["comerciales"]]

# Obtener la comisión máxima
comision_max = max(comisiones)

# Imprimir la comisión máxima
print(f"Comisión máxima: {comision_max}")

## Desarrollado por BRAYAN YESID LINDARTE ANAYA - 1010120365 