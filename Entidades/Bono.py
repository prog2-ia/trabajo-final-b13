class Bono(Activo):
    def __init__(self, nombre, ticker, precio_actual, tasa_inter, vencimiento):
        super().__init__(nombre, ticker, precio_actual)
        self._tasa_interes = tasa_interes
        self._vencimiento = vencimiento

    def calcular_riesgo(self) -> str:
        # Los bonos suelen considerarse de riesgo bajo
        return "Bajo"

    def __str__(self):
        return f"Bono: {super().__str__()} | Interés: {self._tasa_interes}%"