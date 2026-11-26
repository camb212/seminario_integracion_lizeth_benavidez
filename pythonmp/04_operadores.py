print("OPERADORES")
print("Operadores Aritmeticos")

print("+ Suma:", 450, "+", 50, "=", 450 + 50)
print("- Resta:", 500, "-", 50, "=", 500 - 50)
print("* Multiplicacion:", 450, "*", 3, "=", 450 * 3)
print("/ Division:", 1500, "/", 3, "=", 1500 / 3)
print("// Division Entera:", 1000, "//", 3, "=", 1000 // 3)
print("% Residuo:", 1000, "%", 3, "=", 1000 % 3)
print("** Potencia:", 2, "**", 3, "=", 2 ** 3)

print("Tabla de multiplicar del precio de un paquete turistico: $50")

print(50, "*", 1, "=", 50 * 1)
print(50, "*", 2, "=", 50 * 2)
print(50, "*", 3, "=", 50 * 3)
print(50, "*", 4, "=", 50 * 4)
print(50, "*", 5, "=", 50 * 5)
print(50, "*", 6, "=", 50 * 6)
print(50, "*", 7, "=", 50 * 7)
print(50, "*", 8, "=", 50 * 8)
print(50, "*", 9, "=", 50 * 9)
print(50, "*", 10, "=", 50 * 10)

print("OPERADORES DE COMPARACION")

print("== Igual a:", 500, "==", 500, "=", 500 == 500)
print("== Igual a:", 500, "==", 400, "=", 500 == 400)
print("!= Diferente de:", 500, "!=", 500, "=", 500 != 500)
print("> Mayor que:", 500, ">", 300, "=", 500 > 300)
print("> Mayor que:", 500, ">", 800, "=", 500 > 800)
print("< Menor que:", 300, "<", 500, "=", 300 < 500)
print("< Menor que:", 800, "<", 500, "=", 800 < 500)
print(">= Mayor o igual que:", 500, ">=", 800, "=", 500 >= 800)
print(">= Mayor o igual que:", 500, ">=", 300, "=", 500 >= 300)
print("<= Menor o igual que:", 500, "<=", 800, "=", 500 <= 800)
print("<= Menor o igual que:", 500, "<=", 300, "=", 500 <= 300)

print("OPERADORES LOGICOS")

print("Operador and: (500==500) and (300>200)", (500 == 500) and (300 > 200))
print("Operador and: (500==500) and (300>800)", (500 == 500) and (300 > 800))
print("Operador or: (500==500) or (300>800)", (500 == 500) or (300 > 800))
print("Operador or: (500==600) or (300>800)", (500 == 600) or (300 > 800))
print("Operador not: not (500==600)", not (500 == 600))
print("Operador not: not (500==500)", not (500 == 500))

tiene_dinero = True
paquete_disponible = False
puede_reservar = tiene_dinero and paquete_disponible
print("¿Puede reservar el viaje?", puede_reservar)

es_cliente_vip = True
tiene_dinero = False
acceso_credito = es_cliente_vip or tiene_dinero
print("¿Puede acceder al credito?", acceso_credito)