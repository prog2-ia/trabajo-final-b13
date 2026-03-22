class Etiqueta:
    """
        Representa una marca o categoría personalizada para organizar los activos.
    """
    def __init__(self, nombre,tipo):
        """
                Constructor para definir el nombre de la etiqueta y su categoría (tipo).
        """
        self.nombre=nombre
        self.tipo=tipo

    def __str__(self):
        """
                Muestra la etiqueta de forma clara.
        """
        return f'Etiqueta: {self.nombre} | Tipo: {self.tipo}'
