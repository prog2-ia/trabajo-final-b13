from abc import ABC, abstractmethod

class Activo(ABC):
    def __init__(self,nombre, ticket,precio_actual)
        self.nombre = nombre
        self.ticket = ticket
        self.precio_actual = precio_actual

        @abstractmethod
        def actualizar_precio(self):
            pass

        def __str__(self):
            return f"{self.nombre} ({self.ticker}) - Precio: {self.precio_actual:.2f}€"