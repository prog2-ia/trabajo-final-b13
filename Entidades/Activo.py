from abc import ABC, abstractmethod

class Activo(ABC):
    def __init__(self, nombre, ticker, precio_actual):

        self._nombre = nombre
        self._ticker = ticker
        self._precio_actual = precio_actual

    @abstractmethod
    def actualizar_precio(self, nuevo_precio: float):
        pass

    def __str__(self):

        return f"{self._nombre} ({self._ticker}) - Precio: {self._precio_actual:.2f}€"