"""
Manejo de caracteres
"""

nombre1= "Qui-Gon Jin"
print(f"Jedi 1: {nombre1}")
print(f"Tipo de datos: {type(nombre1)}")

nombre2= "Obiwan Kenobi"
print(f"Jedi 1: {nombre2}")
print(f"Tipo de datos: {type(nombre2)}")

###### Funciones comunes de las variables String
print("Funciones comunes de texto")
droide_1 = "R2-D2"
droide_2 = "C3PO"

longitud_droide_1 = len(droide_1)
longitud_droide_2 = len(droide_2) 
print("Nombre droide 1: ", droide_1)
print("Longitud droide 1: ", longitud_droide_1)

print("Nombre droide 2: ", droide_2)
print("Longitud droide 2: ", longitud_droide_2)

print("Convertir Mayusculas y minisculas")
mesnaje = "La federacion invade el planeta NABOO"
mensaje_mayuscula = mesnaje.upper()
mensaje_minuscula = mesnaje.lower()
print("Mensaje en Mayuscula: ", mensaje_mayuscula)
print("Mensaje en minuscula: ", mensaje_minuscula)

print("Reemplazo de substring ")
mensaje = "La nave viaja a Tatooine"
nuevo_mensaje = mensaje.replace("Tatooine", "Coruscant")
print("Mensaje original: ",mensaje)
print("Nuevo mensaje: ", nuevo_mensaje)

print("Separaciòn de cadenas en un arreglo")
planetas = "Naboo,Tatooine,Kmino"
print("planetas: ", planetas)
lista_planetas = planetas.split(",")
print(lista_planetas)
print("Primer planeta : ", lista_planetas[0])

print("Extraer subcadenas")
mensaje = "Que la fuerza te acompañe siempre"
adjetivo = mensaje[7:13]
verbo = mensaje[17:25]
print("adjetivo es : ", adjetivo)
print("verbo es : ", verbo)

print("Comprobaciones útiles")
codigo = "R2D2"
numero = "2026"
nombre = "Univesidad UTE"
identificador = "DROIDE1"
print(codigo.isalnum())
print(numero.isdigit())
print(nombre.isalpha())
print(identificador.isalnum())
print(identificador.isdigit())