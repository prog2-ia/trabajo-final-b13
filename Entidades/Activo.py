from abc import ABC, abstractmethod

class Activo(ABC):
    """
        Clase abstracta que representa un activo financiero genérico.
        Define la estructura base para cualquier tipo de activo (ej. Accion, Criptomoneda).
        """

    def __init__(self, nombre, ticker, precio_actual):
        """
                Constructor de la clase Activo.
                Usa atributos protegidos (_) para asegurar el encapsulamiento.
        """
        self._nombre = nombre
        self._ticker = ticker
        self._precio_actual = precio_actual

    @abstractmethod
    def actualizar_precio(self, nuevo_precio: float):
        """
                Método abstracto que obliga a las clases hijas a implementar
                su propia lógica de actualización de precios.
        """
        pass

    def __str__(self):
        """
                Devuelve una representación en cadena del activo para facilitar su lectura.
        """
        return f"{self._nombre} ({self._ticker}) - Precio: {self._precio_actual:.2f}€"