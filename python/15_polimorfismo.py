class Personaje:
    nombre: str
    raza: str

    def __init__(self, nombre:str, raza:str):
        self.nombre = nombre
        self.raza = raza

    def mostrar_info(self):
        print("Nombre: ", self.nombre)
        print("Raza: ", self.raza)

class Saiyayin(Personaje):
    def __init__(self, nombre:str, raza:str):
        super().__init__(nombre, raza)

    def mostrar_info(self):
        print("El nombre supersaiyayin : ", self.nombre, "Raza: ", self.raza)

goku = Saiyayin("Goku", "Saiyayin")
vegeta = Saiyayin("Vegeta", "Saiyayin")
goku.mostrar_info()
vegeta.mostrar_info()