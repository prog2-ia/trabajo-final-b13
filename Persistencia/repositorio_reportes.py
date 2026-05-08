import os

class RepositorioReportes:
    """
    Se encarga de emitir reportes y extractos en formato de texto plano.
    """
    def __init__(self, directorio_base: str = "data"):
        self.__directorio_base = directorio_base
        self.__asegurar_directorio()

    def __asegurar_directorio(self) -> None:
        """Comprueba si la carpeta 'data' existe, si no, la crea."""
        if not os.path.exists(self.__directorio_base):
            os.makedirs(self.__directorio_base)

    def generar_reporte(self, nombre_fichero: str, contenido: str) -> bool:
        """
        Guarda una cadena de texto en un fichero .txt o .csv.
        """
        ruta = os.path.join(self.__directorio_base, nombre_fichero)
        try:
            with open(ruta, 'w', encoding='utf-8') as f:
                f.write(contenido)
            return True
        except IOError as e:
            raise Exception(f"Error al escribir el reporte: {e}")