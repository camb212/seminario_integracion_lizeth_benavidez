
"""
Manejo de cadena de caracteres
"""

nombre1 = "Camila Benavidez"
print(f"Cliente 1: {nombre1}")
print(f"Tipo de dato: {type(nombre1)}")

nombre2 = "Danny Guaman"
print(f"Cliente 2: {nombre2}")
print(f"Tipo de dato: {type(nombre2)}")


print("Funciones comunes de texto")

destino_1 = "Quito"
destino_2 = "Galapagos"

longitud_destino_1 = len(destino_1)
longitud_destino_2 = len(destino_2)

print("Nombre destino 1:", destino_1)
print("Longitud destino 1:", longitud_destino_1)
print("Nombre destino 2:", destino_2)
print("Longitud destino 2:", longitud_destino_2)


print("Convertir a mayusculas y minusculas")

mensaje = "bienvenido a nuestra agencia de viajes"
mensaje_mayusculas = mensaje.upper()
mensaje_minusculas = mensaje.lower()

print("Mensaje original:", mensaje)
print("Mensaje en mayusculas:", mensaje_mayusculas)
print("Mensaje en minusculas:", mensaje_minusculas)


print("Reemplazo de substring")

mensaje = "viaja a quito con nuestra agencia"
nuevo_mensaje = mensaje.replace("quito", "guayaquil")

print("Mensaje original:", mensaje)
print("Mensaje reemplazado:", nuevo_mensaje)


print("Separacion de cadenas en un arreglo")

destinos = "Quito, Guayaquil, Cuenca"
print("Destinos:", destinos)

lista_destinos = destinos.split(", ")

print("Lista de destinos")
print("Primer destino:", lista_destinos[0])


print("Extraer subcadenas")

mensaje = "Reserva tu viaje hoy mismo"
adjetivo = mensaje[12:17]
verbo = mensaje[0:7]

print("Palabra extraida 1:", adjetivo)
print("Palabra extraida 2:", verbo)


print("Comprobaciones utiles")

codigo = "VIAJE2026"
numero = "2026"
nombre = "Agencia"
identificacion = "CLIENTE1"

print(codigo.isalnum())
print(numero.isnumeric())
print(nombre.isalpha())
print(identificacion.isalnum())
print(identificacion.isdigit())