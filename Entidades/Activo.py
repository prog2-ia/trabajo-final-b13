from abc import ABC, abstractmethod

class Activo(ABC):
    def __init__(self, nombre: str, ticker: str, precio_actual: float):

        self._nombre = nombre
        self._ticker = ticker
        self._precio_actual = precio_actual

    @abstractmethod
    def actualizar_precio(self, nuevo_precio: float):
        """Este método es obligatorio para los hijos (Herencia) [cite: 491]"""
        pass

    def __str__(self):

        return f"{self._nombre} ({self._ticker}) - Precio: {self._precio_actual:.2f}€"