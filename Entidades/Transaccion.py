class Transaccion:
    def __init__(self, tipo, ticker, cantidad, precio_ejecucion):
        self._fecha = datetime.now()
        self._tipo = tipo  # "COMPRA" o "VENTA"
        self._ticker = ticker
        self._cantidad = cantidad
        self._precio_ejecucion = precio_ejecucion

    def obtener_monto_total(self):
        return self._cantidad * self._precio_ejecucion