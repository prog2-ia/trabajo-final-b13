class Divisa:
    """
        Representa una moneda extranjera utilizada para la valoración de activos.
    """
    def __init__(self, nombre, codigo, simbolo):
        self.nombre = nombre    # Ej: "Dólar Estadounidense"
        self.codigo = codigo    # Ej: "USD"
        self.simbolo = simbolo  # Ej: "$"

    def __str__(self):
        """
                Muestra la divisa de forma legible.
        """
        return f"{self.nombre} ({self.simbolo})"