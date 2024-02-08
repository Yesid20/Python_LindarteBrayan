import json

# Cargar datos
with open("data.json") as f:
    data = json.load(f)

def crear(conjunto, datos):
    data[conjunto].append(datos)
    guardar_datos()

def leer(conjunto):
    return data[conjunto]

def actualizar(conjunto, id, datos):
    indice = encontrar_indice(conjunto, id)
    if indice is not None:
        data[conjunto][indice] = datos
        guardar_datos()

def eliminar(conjunto, id):
    indice = encontrar_indice(conjunto, id)
    if indice is not None:
        del data[conjunto][indice]
        guardar_datos()

def encontrar_indice(conjunto, id):
    for i, elemento in enumerate(data[conjunto]):
        if elemento["id"] == id:
            return i
    return None

def guardar_datos():
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

