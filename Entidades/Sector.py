class Sector:
    """
        Clase que define el sector económico de un activo.
    """
    def __init__(self,nombre,volatilidad):
        """
                Constructor para asignar el nombre del sector y su nivel de riesgo.
        """
        self.nombre=nombre
        self.volatilidad=volatilidad

    def __str__(self):
        return f'{self.nombre} (Riesgo): {self.volatilidad}'
