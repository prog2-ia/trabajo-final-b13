class Inversor:
    def __init__(self, nombre: str, id_usuario: int):
        self._nombre = nombre
        self._id_usuario = id_usuario
        self._carteras: list['Cartera'] = []  # Lista de objetos de tipo Cartera [cite: 20, 39]

    def agregar_cartera(self, cartera: 'Cartera'):
        self._carteras.append(cartera)

    def calcular_patrimonio_total(self):
        return sum(c.valor_total() for c in self._carteras)