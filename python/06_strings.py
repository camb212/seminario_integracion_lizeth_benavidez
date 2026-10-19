"""
Manejo de cadena de caracteres
"""

nombre1= "Qui-Gon Jin"
print(f"Jedi 1: {nombre1}")
print(f"Tipo de dato: {type(nombre1)}")
nombre2= "Obi-Wan Kenobi"
print(f"Jedi 2: {nombre2}")
print(f"Tipo de dato: {type(nombre2)}")

print("Funciones comunes texto")
droide_1 = "R2-D2"
droide_2 = "C-3PO"
logintud_droide_1 = len(droide_1)
logintud_droide_2 = len(droide_2)
print("nombre droide 1", droide_1)
print("longitud droide 1", logintud_droide_1)
print("nombre droide 2", droide_2)
print("longitud droide 2", logintud_droide_2)

print("Convertir a mayusculas y minusculas")
mensaje = "la federacion invade el planeta naboo"
mensaje_mayusculas = mensaje.upper()
mensaje_minusculas = mensaje.lower()
print("mensaje original", mensaje)
print("mensaje en mayusculas", mensaje_mayusculas)
print("mensaje en minusculas", mensaje_minusculas)

print("remplazo de substring")
mensaje = "la nave viajera a tatooine"
nuevo_mensaje = mensaje.replace("tatooine", "coruscant")
print("mensaje original", mensaje)
print("mensaje reemplazado", nuevo_mensaje)


print("separacion de cadenas en un arreglo")
planetas = "naboo, tatooine, kmino"
print("planetas", planetas)
lista_planetas = planetas.split(", ")
print("lista de planetas")
print("primer planeta:", lista_planetas[0])

print("extraer subcadenas")
mensaje = "Que la fuerza te acompañe siempre"
adjetivo = mensaje[7:12]
verbo = mensaje[18:25]
print("adjetivo es: ", adjetivo)
print("verbo es: ", verbo)

print("comprobaciones utiles")
codigo = "R2D2"
numero = "2026"
nombre = "Universidad Ute"
indentificacion = "DROIDE1"
print(codigo.isalnum())
print(numero.isnumeric())
print(nombre.isalpha())
print(indentificacion.isalnum())
print(indentificacion.isdigit())


