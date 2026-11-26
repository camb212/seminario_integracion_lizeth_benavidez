class MaterialBiblioteca:
    titulo: str
    categoria: str

    def __init__(self, titulo: str, categoria: str):
        self.titulo = titulo
        self.categoria = categoria

    def mostrar_info(self):
        print("Título: ", self.titulo)
        print("Categoría: ", self.categoria)

class Libro(MaterialBiblioteca):
    def __init__(self, titulo: str, categoria: str):
        super().__init__(titulo, categoria)

    def mostrar_info(self):
        print("El título del libro es: ", self.titulo, "Categoría: ", self.categoria)

libro_1 = Libro("Cien años de soledad", "Novela")
libro_2 = Libro("Clean Code", "Programación")
libro_1.mostrar_info()
libro_2.mostrar_info()
