class Alerta:
    def __init__(self, ticker, precio_umbral, tipo_alerta):
        self._ticker = ticker
        self._precio_umbral = precio_umbral
        self._tipo_alerta = tipo_alerta  # "SUBIDA" o "BAJADA"
        self._activa = True

    def verificar(self, precio_actual: float) -> bool:
        if self._tipo_alerta == "BAJADA":
            return precio_actual <= self._precio_umbral
        return precio_actual >= self._precio_umbral