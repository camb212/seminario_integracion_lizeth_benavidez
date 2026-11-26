class PaqueteTuristico():
    destino: str
    __codigo_interno: int

    def __init__(self, destino: str, codigo_interno: int):
        self.destino = destino
        self.__codigo_interno = codigo_interno

    def mostrar_inf(self):
        print("Destino:", self.destino)
        print("Código Interno (Confidencial):", self.__codigo_interno)

    def get_codigo_interno(self):
        return self.__codigo_interno


paquete1 = PaqueteTuristico("Galápagos", 1010)
paquete2 = PaqueteTuristico("Cuenca", 1020)
paquete3 = PaqueteTuristico("Baños", 1030)
paquete4 = PaqueteTuristico("Quito", 9999)

paquete1.mostrar_inf()
paquete2.mostrar_inf()
paquete3.mostrar_inf()
paquete4.mostrar_inf()

print("Acceso público directo al destino del paquete 1:", paquete1.destino)
print("Acceso público directo al destino del paquete 2:", paquete2.destino)