print("Incluir datos con Input")

nombre = input("¿Cual es el nombre del cliente? ")
print("¡Hola", nombre, "!")
print("Bienvenido a nuestra agencia de viajes")
print("Hasta luego " + nombre)

cantidad = int(input("¿Cuantos pasajeros viajaran? "))
total = cantidad + 2
print("Pasajeros totales: ", total)

print("Conversiones")
print("==== Agencia de Viajes Ecuador ====")

nombre_cliente = input("Nombre del cliente: ")
precio = float(input("Precio del paquete turistico: "))
cantidad = int(input("Cantidad de paquetes turisticos: "))

total = precio * cantidad

print("Total a pagar:", total)
print("Total a pagar (round):", round(total, 2))
print(f"Total a pagar (f): {total:.2f}")