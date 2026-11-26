print("Incluir datos con Input")
nombre=input("¿Cual es el nombre?")
print("!Hola", nombre, "!")
print("Bienvenido a Springfield")
print("Hasta luego " +nombre)

cantidad = int(input("¿Cuantas rosquillas hay?"))
total = cantidad + 2
print ("Rosquillas totales: ", total)

print(" Conversiones")
print("====Tienda de Apu====")
nombre_cliente = input("Nombre del cliente: ")
precio = float(input("Precio del producto: "))
cantidad = int(input("Cantidad de productos: "))
total = precio * cantidad
print("Total a pagar:", total)
print("Total a pagar (round):", round(total, 2))
print(f"Total a pagar (f): {total:.2f}")