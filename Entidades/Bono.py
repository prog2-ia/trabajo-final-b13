class Bono(Activo):
    """
        Representa un bono financiero que hereda de la clase abstracta Activo.
        Demuestra el uso de Herencia y Polimorfismo.
    """
    def __init__(self, nombre, ticker, precio_actual, tasa_interes, vencimiento):
        """
                Constructor que utiliza super() para inicializar los atributos de la clase base.
        """
        super().__init__(nombre, ticker, precio_actual)
        self._tasa_interes = tasa_interes
        self._vencimiento = vencimiento

    def calcular_riesgo(self):
        """
                Método específico de la clase Bono para evaluar su nivel de riesgo.
        """
        # Los bonos suelen considerarse de riesgo bajo
        return "Bajo"

    def __str__(self):
        """
                Sobrescribe el método __str__ usando la lógica de la clase padre
                y añadiendo información específica del bono.
        """
        return f"Bono: {super().__str__()} | Interés: {self._tasa_interes}%"