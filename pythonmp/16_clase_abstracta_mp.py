from abc import ABC, abstractmethod

class ServicioAgencia(ABC):
    @abstractmethod
    def reservar(self):
        pass


class PaqueteTuristico(ServicioAgencia):
    def reservar(self):
        return "Paquete turístico reservado por 15 días"


paquete = PaqueteTuristico()
print(paquete.reservar())