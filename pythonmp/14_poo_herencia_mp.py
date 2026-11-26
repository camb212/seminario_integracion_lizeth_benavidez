class ServicioAgencia:
    destino: str
    categoria: str

    def __init__(self, destino: str, categoria: str):
        self.destino = destino
        self.categoria = categoria

    def mostrar_info(self):
        print("Destino: ", self.destino)
        print("Categoría: ", self.categoria)


class PaqueteTuristico(ServicioAgencia):
    def __init__(self, destino: str, categoria: str):
        super().__init__(destino, categoria)

    def muestra_destino(self):
        print("Destino: ", self.destino)


paquete_1 = PaqueteTuristico("Galápagos", "Playa")
paquete_2 = PaqueteTuristico("Baños", "Aventura")

paquete_1.mostrar_info()
paquete_2.mostrar_info()
paquete_1.muestra_destino()
paquete_2.muestra_destino()