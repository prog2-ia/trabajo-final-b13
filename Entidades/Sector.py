class Sector:
    def __init__(self,nombre,volatilidad):
        self.nombre=nombre
        self.volatilidad=volatilidad

    def __str__(self):
        return f'{self.nombre} (Riesgo): {self.volatilidad}'
