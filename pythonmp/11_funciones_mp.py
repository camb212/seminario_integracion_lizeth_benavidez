print("Módulo de Funciones de la Biblioteca")
print("Autor: Andrés Jurado")

def registrar_ingreso():
    print("Verificando código de barras del libro...")
    print("Libro registrado exitosamente en el sistema")

registrar_ingreso()
registrar_ingreso()
registrar_ingreso()
registrar_ingreso()

def prestar_libro(usuario):
    print(f"Se ha procesado el préstamo de un ejemplar para el usuario: {usuario}")

prestar_libro("Carlos Pérez")
prestar_libro("María Gómez")
prestar_libro("Lucía Torres")
prestar_libro("Andrés Jurado")

def calcular_multa(dias_retraso, tarifa_diaria):
    multa_total = dias_retraso * tarifa_diaria
    return multa_total

deuda = calcular_multa(4, 0.50)
print("La multa acumulada es de: $", deuda)

deuda_usuario_vip = calcular_multa(10, 0.25)
print("Multa calculada para usuario VIP: $", deuda_usuario_vip)

def verificar_estado_usuario(nombre, libros_prestados):
    if libros_prestados <= 3:
        print(f"El usuario {nombre} está habilitado para solicitar más préstamos")
    else:
        print(f"El usuario {nombre} ha excedido el límite de préstamos permitidos")

verificar_estado_usuario("Francisco Higuera", 2)
verificar_estado_usuario("Anahí Loza", 5)

nombre_obra: str = "Cien Años de Soledad"
codigo_isbn: int = 9780307
precio_referencia: float = 24.99
es_disponible: bool = True

def estimar_valor_inventario(cantidad: int, costo_unitario: float) -> float:
    return cantidad * costo_unitario

valor_total: float = estimar_valor_inventario(15, 24.99)
print("Valor total del lote en inventario: $", valor_total)