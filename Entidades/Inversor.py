class Inversor:
    def __init__(self, nombre, id_usuario):
        self._nombre = nombre
        self._id_usuario = id_usuario
        self._carteras = []  # Lista de objetos de tipo Cartera

    def agregar_cartera(self, cartera: 'Cartera'):
        self._carteras.append(cartera)

    def calcular_patrimonio_total(self):
        return sum(c.valor_total() for c in self._carteras)