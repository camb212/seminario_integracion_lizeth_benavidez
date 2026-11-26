prestamos_activos = 20
limite_capacidad = 100

while prestamos_activos < limite_capacidad:
    print("La biblioteca está recibiendo préstamos, total actual:", prestamos_activos)
    prestamos_activos += 20

print("La biblioteca ha alcanzado su límite operativo óptimo de préstamos")

stock_libro = 50
while stock_libro > 0:
    print("Quedan ", stock_libro, " ejemplares disponibles para préstamo")
    stock_libro -= 10

print("Se agotaron todos los ejemplares de la obra")