from Entidades.Transaccion import Transaccion
from Entidades.RegistroHistorial import RegistroHistorial
from Servicios.gestion_mercado import GestionMercado
from Servicios.gestion_inversores import GestionInversores
from Servicios.excepciones import ImporteInvalidoException, LimiteSuperadoException
from Persistencia.repositorio_reportes import RepositorioReportes


class GestionTransacciones:
    def __init__(self, mercado: GestionMercado, inversores: GestionInversores, repo_reportes: RepositorioReportes):
        # Inyectamos las dependencias
        self.mercado = mercado
        self.gestor_inversores = inversores
        self.repo_reportes = repo_reportes
        self.log_eventos = []

    def ejecutar_compra(self, id_inversor: str, ticker: str, cantidad: float) -> Transaccion:
        # 1. Validar la cantidad
        if cantidad <= 0:
            raise ImporteInvalidoException("La cantidad a comprar debe ser mayor a 0.")

        # 2. Recuperar el activo y el inversor desde los otros gestores
        activo = self.mercado.obtener_activo(ticker)
        inversor = self.gestor_inversores.obtener_inversor(id_inversor)

        # 3. Crear la transacción
        transaccion = Transaccion(tipo="COMPRA", ticker=ticker, cantidad=cantidad,
                                  precio_ejecucion=activo._precio_actual)
        coste_total = transaccion.obtener_monto_total()

        # TODO: Añadir aquí la validación de la Cartera cuando la creemos.
        # if inversor.cartera.saldo < coste_total:
        #     raise LimiteSuperadoException("Saldo insuficiente.")

        # 4. Registrar en el historial
        evento = RegistroHistorial("COMPRA", f"{inversor._nombre} compró {cantidad} de {ticker}")
        self.log_eventos.append(evento)

        return transaccion

    def generar_reporte_usuario(self, id_inversor: str) -> bool:
        inversor = self.gestor_inversores.obtener_inversor(id_inversor)

        # Formateamos los datos como texto
        contenido = f"--- REPORTE DE INVERSOR ---\n"
        contenido += f"Nombre: {inversor._nombre}\n"
        contenido += f"Patrimonio Total: {inversor.calcular_patrimonio_total()}€\n"

        # Delegamos a Persistencia que lo guarde
        nombre_fichero = f"reporte_{id_inversor}.txt"
        return self.repo_reportes.generar_reporte(nombre_fichero, contenido)