from abc import ABC, abstractmethod

class MaterialBiblioteca(ABC):
    @abstractmethod
    def prestar(self):
        pass

class Libro(MaterialBiblioteca):
    def prestar(self):
        return "Libro prestado por 15 días"

libro = Libro()
print(libro.prestar())
