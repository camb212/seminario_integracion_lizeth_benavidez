class LibroBiblioteca:
    titulo: str
    isbn: str
    
    def __init__(self, titulo: str, isbn: str):
        self.titulo = titulo
        self.isbn = isbn

    def mostrar_inf(self):
        print("Título del libro:", self.titulo)
        print("ISBN:", self.isbn)

libro1 = LibroBiblioteca("Cien Años de Soledad", "978-0307474728")
libro2 = LibroBiblioteca("Don Quijote de la Mancha", "978-8424116033")
libro3 = LibroBiblioteca("El Principito", "978-0156013987")
libro4 = LibroBiblioteca("Clean Code", "978-0132350884")

libro1.mostrar_inf()
libro2.mostrar_inf()
libro3.mostrar_inf()
libro4.mostrar_inf()