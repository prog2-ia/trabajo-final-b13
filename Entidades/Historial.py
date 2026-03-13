class RegistroHistorial:
    def __init__(self, tipo_evento, descripcion):
        self.tipo_evento = tipo_evento  # Ej: "COMPRA", "VENTA", "CAMBIO_PRECIO"
        self.descripcion = descripcion
        self.timestamp = datetime.now()

    def __str__(self):
        ts = self.timestamp.strftime("%H:%M:%S")
        return f"{ts} - {self.tipo_evento}: {self.descripcion}"