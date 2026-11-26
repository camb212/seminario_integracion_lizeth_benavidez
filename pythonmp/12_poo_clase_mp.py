class PaqueteTuristico:
    destino: str
    codigo: str

    def __init__(self, destino: str, codigo: str):
        self.destino = destino
        self.codigo = codigo

    def mostrar_inf(self):
        print("Destino del viaje:", self.destino)
        print("Código del paquete:", self.codigo)


paquete1 = PaqueteTuristico("Galápagos", "PKG-001")
paquete2 = PaqueteTuristico("Cuenca", "PKG-002")
paquete3 = PaqueteTuristico("Baños", "PKG-003")
paquete4 = PaqueteTuristico("Quito", "PKG-004")

paquete1.mostrar_inf()
paquete2.mostrar_inf()
paquete3.mostrar_inf()
paquete4.mostrar_inf()