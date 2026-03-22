from datetime import datetime
class RegistroHistorial:
    """
        Clase encargada de documentar eventos específicos dentro del sistema
        para mantener un log de auditoría.
    """
    def __init__(self, tipo_evento, descripcion):
        """
                Constructor que registra el tipo de evento, su descripción
                y el momento exacto (timestamp) en que ocurre.
            """
        self.tipo_evento = tipo_evento  # Ej: "COMPRA", "VENTA", "CAMBIO_PRECIO"
        self.descripcion = descripcion
        self.timestamp = datetime.now()

    def __str__(self):
        """
                Devuelve el registro formateado con la hora exacta del evento.
        """
        ts = self.timestamp.strftime("%H:%M:%S")
        return f"{ts} - {self.tipo_evento}: {self.descripcion}"