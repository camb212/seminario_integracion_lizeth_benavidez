for reserva in range(1, 6):
    print("Confirmación de reserva #", reserva)

for paquete_id in range(1, 11):
    print("Costo adicional por día de hospedaje:", 10, "*", paquete_id, "=", 10 * paquete_id)

for paquete_id in range(1, 11, 2):
    print("Descuento especial por días de viaje:", 10, "*", paquete_id, "=", 10 * paquete_id)

paquetes = [
    {"id": 1, "destino": "Galápagos", "precio": 500, "estado": "Disponible"},
    {"id": 2, "destino": "Cuenca", "precio": 150, "estado": "Disponible"},
    {"id": 3, "destino": "Baños", "precio": 100, "estado": "Disponible"}
]

print("Lista de paquetes turísticos:")
for paquete in paquetes:
    print(f"{paquete['id']} - Destino: {paquete['destino']}")

destinos = ["Galápagos", "Quito", "Cuenca"]
for destino in destinos:
    print("Destino actual en catálogo: ", destino)

cupos_disponibles = {
    "Galápagos": 12,
    "Cuenca": 4,
    "Baños": 3,
    "Quito": 8
}

for destino, cupos in cupos_disponibles.items():
    if cupos >= 5:
        print(destino, "tiene suficientes cupos disponibles")
    else:
        print(destino, "requiere más cupos para las reservas")

print("Ciclo anidado para revisar paquetes turísticos:")
sucursales = ["Sucursal Norte", "Sucursal Sur", "Sucursal Centro", "Sucursal Valle"]

for sucursal in sucursales:
    print("Revisando sucursal:", sucursal)
    for paquete in range(1, 4):
        print("Paquete turístico revisado: ", paquete)

print("Uso de Break y Continue en búsqueda de destinos:")
for sucursal in sucursales:
    print("Sucursal actual: ", sucursal)
    if sucursal == "Sucursal Centro":
        break
    elif sucursal == "Sucursal Sur":
        continue
    print("Sucursal verificada con éxito: ", sucursal)