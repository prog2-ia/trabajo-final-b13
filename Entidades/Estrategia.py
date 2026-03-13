class Estrategia:
    def __init__(self, nombre):
        self._nombre = nombre
        self._pesos_objetivo = {}  # {ticker: porcentaje (0.0 a 1.0)}

    def definir_peso(self, ticker, porcentaje):
        self._pesos_objetivo[ticker] = porcentaje

    def es_valida(self):
        # La suma de pesos debe ser 100% (1.0)
        return sum(self._pesos_objetivo.values()) == 1.0