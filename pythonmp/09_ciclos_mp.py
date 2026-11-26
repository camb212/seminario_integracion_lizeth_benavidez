for prestamo in range(1, 6):
    print("Renovación de préstamo #", prestamo)

for libro_id in range(1, 11):
    print("Costo de multa por día atrasado:", 0.50, "*", libro_id, "=", 0.50 * libro_id)

for libro_id in range(1, 11, 2):
    print("Tarifa especial por días acumulados:", 0.50, "*", libro_id, "=", 0.50 * libro_id)

libros = [
    {"id": 1, "titulo": "Cien Años de Soledad", "autor": "Gabriel García Márquez", "estado": "Disponible"},
    {"id": 2, "titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "estado": "Disponible"},
    {"id": 3, "titulo": "El Principito", "autor": "Antoine de Saint-Exupéry", "estado": "Disponible"}
]

print("Lista de libros en inventario:")
for libro in libros:
    print(f"{libro['id']} - Título: {libro['titulo']}")

autores = ["Gabriel García Márquez", "Jorge Luis Borges", "Mario Vargas Llosa"]
for autor in autores:
    print("Autor actual en catálogo: ", autor)

ejemplares_disponibles = {
    "Cien Años de Soledad": 12,
    "Don Quijote de la Mancha": 4,
    "Rayuela": 3,
    "El Aleph": 2
}

for titulo, stock in ejemplares_disponibles.items():
    if stock >= 5:
        print(titulo, "tiene suficiente stock disponible")
    else:
        print(titulo, "requiere reposición urgente de ejemplares")

print("Ciclo anidado para inventario físico por estantería:")
estanterias = ["Estante A", "Estante B", "Estante C", "Estante D"]
for estante in estanterias:
    print("Revisando sección:", estante)
    for pasillo in range(1, 4):
        print("Pasillo revisado: ", pasillo)

print("Uso de Break y Continue en búsqueda de libros:")
for estante in estanterias:
    print("Estante actual: ", estante)
    if estante == "Estante C":
        break
    elif estante == "Estante B":
        continue
    print("Estante verificado con éxito: ", estante)