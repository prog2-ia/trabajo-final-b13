import os
import pickle
from typing import Any, Optional

class RepositorioPartidas:
    """
    Se encarga de guardar y cargar el estado del simulador de bolsa
    en formato binario (pickle).
    """
    def __init__(self, directorio_base: str = "data"):
        self.__directorio_base = directorio_base
        self.__asegurar_directorio()

    def __asegurar_directorio(self) -> None:
        """Comprueba si la carpeta 'data' existe, si no, la crea."""
        if not os.path.exists(self.__directorio_base):
            os.makedirs(self.__directorio_base)

    def guardar_partida(self, nombre_fichero: str, datos: Any) -> bool:
        """
        Guarda los objetos (carteras, inversores) en un fichero binario.
        """
        ruta = os.path.join(self.__directorio_base, nombre_fichero)
        try:
            with open(ruta, 'wb') as f:
                pickle.dump(datos, f)
            return True
        except IOError as e:
            raise Exception(f"Error crítico de disco al guardar la partida: {e}")

    def cargar_partida(self, nombre_fichero: str) -> Optional[Any]:
        """
        Carga los datos desde un fichero binario. Si no existe, devuelve None.
        """
        ruta = os.path.join(self.__directorio_base, nombre_fichero)
        try:
            with open(ruta, 'rb') as f:
                datos = pickle.load(f)
            return datos
        except FileNotFoundError:
            return None
        except (IOError, pickle.PickleError) as e:
            raise Exception(f"Error al cargar la partida (fichero corrupto): {e}")