class Transaccion:
    """
        Registra los detalles de una operación de compra o venta de un activo.
    """
    def __init__(self, tipo, ticker, cantidad, precio_ejecucion):
        """
                Constructor que inicializa los datos de la operación y registra la fecha actual.
                Usa atributos protegidos (_) para cumplir con el encapsulamiento.
        """
        self._fecha = datetime.now()
        self._tipo = tipo  # "COMPRA" o "VENTA"
        self._ticker = ticker
        self._cantidad = cantidad
        self._precio_ejecucion = precio_ejecucion

    def obtener_monto_total(self):
        """
                Calcula el valor total de la transacción (cantidad x precio).
        """
        return self._cantidad * self._precio_ejecucion