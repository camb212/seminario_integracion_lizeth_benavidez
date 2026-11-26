
print('CRUD DE LISTAS EN PYTHON')

viajes = [
    {'id': 1, 'Destino': 'Galapagos', 'Transporte': 'Avion', 'estado': 'Disponible'},
    {'id': 2, 'Destino': 'Cuenca', 'Transporte': 'Bus', 'estado': 'Disponible'},
    {'id': 3, 'Destino': 'Quito', 'Transporte': 'Avion', 'estado': 'Reservado'}
]

id_publico = 4

def create():
    global id_publico
    print('Registrar viaje')
    destino = input('Destino del viaje: ')
    transporte = input('Transporte (Avion, Bus, Auto): ')
    estado = input('Estado (Disponible, Reservado, Cancelado): ')

    nuevo_viaje = {
        'id': id_publico,
        'Destino': destino,
        'Transporte': transporte,
        'estado': estado
    }

    viajes.append(nuevo_viaje)
    id_publico += 1
    print('Viaje creado correctamente')

def read():
    print('Lista de viajes')
    for viaje in viajes:
        print(f"ID: {viaje['id']}, Destino: {viaje['Destino']}, Transporte: {viaje['Transporte']}, Estado: {viaje['estado']}")

def update():
    print('Actualizar un viaje')
    id_update = int(input('ID a modificar: '))

    for viaje in viajes:
        if viaje['id'] == id_update:
            destino = input('Destino del viaje: ')
            transporte = input('Transporte (Avion, Bus, Auto): ')
            estado = input('Estado (Disponible, Reservado, Cancelado): ')

            viaje['Destino'] = destino
            viaje['Transporte'] = transporte
            viaje['estado'] = estado

            print('Viaje actualizado')
            return

    print('Viaje no encontrado')

def delete():
    print('Eliminar un viaje')
    id_delete = int(input('ID a eliminar: '))

    for viaje in viajes:
        if viaje['id'] == id_delete:
            viajes.remove(viaje)
            print('Viaje eliminado')
            return

    print('Viaje no encontrado')

def menu():
    while True:
        print('\nAgencia de Viajes')
        print('1. Crear viaje')
        print('2. Leer viajes')
        print('3. Modificar viaje')
        print('4. Eliminar viaje')
        print('5. Salir')

        opcion = input('Seleccione del 1 al 5: ')

        if opcion == '1':
            create()
        elif opcion == '2':
            read()
        elif opcion == '3':
            update()
        elif opcion == '4':
            delete()
        elif opcion == '5':
            print('Cerrando sistema')
            break
        else:
            print('Intente con una nueva opcion')

if __name__ == '__main__':
    menu()
