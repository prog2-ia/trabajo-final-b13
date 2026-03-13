class Etiqueta:
    def __init__(self, nombre,tipo):
        self.nombre=nombre
        self.tipo=tipo

    def __str__(self):
        return f'Etiqueta: {self.nombre} | Tipo: {self.tipo}'
