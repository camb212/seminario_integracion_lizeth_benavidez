reservas_activas = 20
limite_capacidad = 100

while reservas_activas < limite_capacidad:
    print("La agencia está recibiendo reservas, total actual:", reservas_activas)
    reservas_activas += 20

print("La agencia ha alcanzado su límite de reservas")

cupos_paquete = 50
while cupos_paquete > 0:
    print("Quedan ", cupos_paquete, " cupos disponibles para viajar")
    cupos_paquete -= 10

print("Se agotaron todos los cupos del paquete turístico")