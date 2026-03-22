class Estrategia:
    """
        Gestiona la distribución de pesos objetivo para una cartera de inversión.
    """
    def __init__(self, nombre):
        """
                Constructor que inicializa el nombre de la estrategia y el diccionario de pesos.
        """
        self._nombre = nombre
        self._pesos_objetivo = {}  # {ticker: porcentaje (0.0 a 1.0)}

    def definir_peso(self, ticker, porcentaje):
        """
                Asigna un peso específico a un activo identificado por su ticker.
        """
        self._pesos_objetivo[ticker] = porcentaje

    def es_valida(self):
        """
                Verifica si la suma de todos los pesos es exactamente el 100% (1.0).
                Devuelve True si es válida, False en caso contrario.
        """
        # La suma de pesos debe ser 100% (1.0)
        return sum(self._pesos_objetivo.values()) == 1.0