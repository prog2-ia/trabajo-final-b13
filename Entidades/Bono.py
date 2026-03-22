from Entidades.Activo import Activo#sino usamos esto no podra acceder a su padre(Activo)

class Bono(Activo):
    def __init__(self, nombre, ticker, precio_actual, tasa_interes, vencimiento):
        super().__init__(nombre, ticker, precio_actual)
        self._tasa_interes = tasa_interes
        self._vencimiento = vencimiento

    def actualizar_precio(self, nuevo_precio: float):
        self._precio_actual = nuevo_precio

    def calcular_riesgo(self):
        # Los bonos suelen considerarse de riesgo bajo
        return "Bajo"

    def __str__(self):
        return f"Bono: {super().__str__()} | Interés: {self._tasa_interes}%"