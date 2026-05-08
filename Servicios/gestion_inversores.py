from typing import Dict
from Entidades.Inversor import Inversor

class GestionInversores:
    def __init__(self):
        self.inversores: Dict[str, Inversor] = {}

    def registrar_inversor(self, inversor: Inversor) -> None:
        self.inversores[inversor._id_usuario] = inversor

    def obtener_inversor(self, id_usuario: str) -> Inversor:
        if id_usuario not in self.inversores:
            raise Exception("El inversor no está registrado en el sistema.")
        return self.inversores[id_usuario]