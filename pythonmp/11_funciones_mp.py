print("Módulo de Funciones de la Agencia de Viajes")
print("Autor: Andrés Jurado")

def registrar_reserva():
    print("Verificando datos de la reserva...")
    print("Reserva registrada exitosamente en el sistema")

registrar_reserva()
registrar_reserva()
registrar_reserva()
registrar_reserva()


def reservar_paquete(usuario):
    print(f"Se ha procesado la reserva de un paquete turístico para el cliente: {usuario}")

reservar_paquete("Carlos Pérez")
reservar_paquete("María Gómez")
reservar_paquete("Lucía Torres")
reservar_paquete("Andrés Jurado")


def calcular_costo(dias_viaje, tarifa_diaria):
    costo_total = dias_viaje * tarifa_diaria
    return costo_total

costo = calcular_costo(4, 50)
print("El costo total del viaje es de: $", costo)

costo_usuario_vip = calcular_costo(10, 25)
print("Costo calculado para cliente VIP: $", costo_usuario_vip)


def verificar_estado_cliente(nombre, reservas_realizadas):
    if reservas_realizadas <= 3:
        print(f"El cliente {nombre} está habilitado para realizar más reservas")
    else:
        print(f"El cliente {nombre} ha excedido el límite de reservas permitidas")

verificar_estado_cliente("Francisco Higuera", 2)
verificar_estado_cliente("Anahí Loza", 5)


nombre_destino: str = "Galápagos"
codigo_paquete: int = 9780307
precio_referencia: float = 24.99
es_disponible: bool = True


def estimar_valor_paquetes(cantidad: int, costo_unitario: float) -> float:
    return cantidad * costo_unitario

valor_total: float = estimar_valor_paquetes(15, 24.99)
print("Valor total de los paquetes turísticos: $", valor_total)