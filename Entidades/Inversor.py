class Inversor:
    """
        Representa al usuario del sistema. Gestiona múltiples carteras de inversión.
    """
    def __init__(self, nombre, id_usuario):
        """
                Inicializa al inversor con su nombre e identificador único.
            """
        self._nombre = nombre
        self._id_usuario = id_usuario
        self._carteras = []  # Lista de objetos de tipo Cartera

    def agregar_cartera(self, cartera: 'Cartera'):
        """
                Añade una nueva cartera a la lista de gestión del inversor.
        """
        self._carteras.append(cartera)

    def calcular_patrimonio_total(self):
        """
                Calcula la suma de los valores de todas las carteras del inversor.
                Demuestra la interacción entre diferentes objetos del sistema.
        """
        return sum(c.valor_total() for c in self._carteras)