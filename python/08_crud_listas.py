
print('CRUD DE LISTAS EN PYTHON')

avengers = [
    {'id': 1, 'Nombre': 'Tony Stark', 'Heroe': 'Iron Man', 'estado': 'Activo'},
    {'id': 2, 'Nombre': 'Steve Rogers', 'Heroe': 'Captain America', 'estado': 'Activo'},
    {'id': 3, 'Nombre': 'Thor Odinson', 'Heroe': 'Thor', 'estado': 'Activo'}
]

id_publico = 4

def create():
    global id_publico
    print('Reclutar Avenger')
    nombre = input('Nombre heroe: ')
    heroe = input('Heroe: ')
    estado = input('Estado (Activo, Retirado, Desaparecido): ')

    nuevo_avenger = {
        'id': id_publico,
        'Nombre': nombre,
        'Heroe': heroe,
        'estado': estado
    }

    avengers.append(nuevo_avenger)
    id_publico += 1
    print('Avenger creado correctamente')

def read():
    print('Lista de Avengers')
    for avenger in avengers:
        print(f"ID: {avenger['id']}, Nombre: {avenger['Nombre']}, Heroe: {avenger['Heroe']}, Estado: {avenger['estado']}")

def update():
    print('Actualizar un Avenger')
    id_update = int(input('ID a modificar: '))

    for avenger in avengers:
        if avenger['id'] == id_update:
            nombre = input('Nombre heroe: ')
            heroe = input('Heroe: ')
            estado = input('Estado (Activo, Retirado, Desaparecido): ')

            avenger['Nombre'] = nombre
            avenger['Heroe'] = heroe
            avenger['estado'] = estado

            print('Avenger actualizado')
            return

    print('Avenger no encontrado')

def delete():
    print('Eliminar un Avenger')
    id_delete = int(input('ID a eliminar: '))

    for avenger in avengers:
        if avenger['id'] == id_delete:
            avengers.remove(avenger)
            print('Avenger eliminado')
            return

    print('Avenger no encontrado')

def menu():
    while True:
        print('\nAvengers')
        print('1. Crear')
        print('2. Leer')
        print('3. Modificar')
        print('4. Eliminar')
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