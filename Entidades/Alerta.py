class Alerta:
    """
        Gestiona avisos automáticos basados en umbrales de precio para un activo.
        Permite monitorizar si un activo sube o baja de cierto valor.
    """
    def __init__(self, ticker, precio_umbral, tipo_alerta):
        """
                Constructor de la alerta.
                Utiliza atributos protegidos (_) para asegurar que la configuración de la
                alerta no se modifique externamente de forma accidental.
        """
        self._ticker = ticker
        self._precio_umbral = precio_umbral
        self._tipo_alerta = tipo_alerta  # "SUBIDA" o "BAJADA"
        self._activa = True

    def verificar(self, precio_actual: float) -> bool:
        """
                Compara el precio actual con el umbral definido.
                Devuelve True si se cumple la condición de la alerta, False en caso contrario.
        """
        if self._tipo_alerta == "BAJADA":
            return precio_actual <= self._precio_umbral
        return precio_actual >= self._precio_umbral