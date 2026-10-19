print("condicional If")
print("Condicional Simple")
dinero=10
if dinero>5:
    print(" Homero puede comprar rosquillas")
print("Programa terminado")

creditos = float(input("Ingrese la cantidad de creditos: "))
precio_respuesta = float(input("Ingrese el precio de la respuesta: "))
if (creditos >= precio_respuesta):
    print("Compra Autorizada")
else:
    print("Credito insuficiente")
    print("buscar solucion o trueque")


print("Condicional if - elif - else")
print("Condicional condiciones Anidadas")
combustible = float(input("Combustible de la nave: "))

if (combustible >= 75):
    print("Optimo")
elif (combustible >= 50):
    print("Suficiente")
elif (combustible >= 20):
    print("Bajo")
else:
    print("Crítico")
    print("Localizar base cercana")


piloto = input ("Nombre del piloto: ")
motor_funciona = input("El motor funciona (si/no): ")
combustible = input("Combustible disponible: ")

if (motor_funciona == "si" ):
    print("motor en funcionamiento")
    if combustible >= 50:
      print("combustible suficiente")
      print("participacion autorizada")
    else:
      print("bebe cargar combustible")
else:
    print("motor no funciona")
    print("participacion no autorizada")
    