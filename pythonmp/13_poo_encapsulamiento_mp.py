class LibroBiblioteca():
    titulo: str
    __codigo_interno: int
    
    def __init__(self, titulo: str, codigo_interno: int):
        self.titulo = titulo
        self.__codigo_interno = codigo_interno

    def mostrar_inf(self):
        print("Título:", self.titulo)
        print("Código Interno (Confidencial):", self.__codigo_interno)

    def get_codigo_interno(self):
        return self.__codigo_interno

libro1 = LibroBiblioteca("Cien Años de Soledad", 1010)
libro2 = LibroBiblioteca("Don Quijote de la Mancha", 1020)
libro3 = LibroBiblioteca("Rayuela", 1030)
libro4 = LibroBiblioteca("Clean Code", 9999)

libro1.mostrar_inf()
libro2.mostrar_inf()
libro3.mostrar_inf()
libro4.mostrar_inf()
print("Acceso público directo al título del libro 1:", libro1.titulo)
print("Acceso público directo al título del libro 2:", libro2.titulo)