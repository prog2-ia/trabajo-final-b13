from typing import Dict
from Entidades.Activo import Activo
from Servicios.excepciones import ActivoDesconocidoException

class GestionMercado:
    def __init__(self):
        # Diccionario para buscar activos rápidamente por su ticker
        self.activos_disponibles: Dict[str, Activo] = {}

    def registrar_activo(self, activo: Activo) -> None:
        self.activos_disponibles[activo._ticker] = activo

    def obtener_activo(self, ticker: str) -> Activo:
        if ticker not in self.activos_disponibles:
            # Lanzamos nuestra excepción personalizada
            raise ActivoDesconocidoException(f"El activo con ticker {ticker} no existe en el mercado.")
        return self.activos_disponibles[ticker]