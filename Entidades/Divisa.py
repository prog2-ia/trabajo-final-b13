class Divisa:
    def __init__(self, nombre, codigo, simbolo):
        self.nombre = nombre    # Ej: "Dólar Estadounidense"
        self.codigo = codigo    # Ej: "USD"
        self.simbolo = simbolo  # Ej: "$"

    def __str__(self):
        return f"{self.nombre} ({self.simbolo})"