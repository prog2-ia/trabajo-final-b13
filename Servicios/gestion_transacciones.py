from Entidades.Transaccion import Transaccion
from Entidades.RegistroHistorial import RegistroHistorial
from Servicios.gestion_mercado import GestionMercado
from Servicios.gestion_inversores import GestionInversores
from Servicios.excepciones import ImporteInvalidoException, LimiteSuperadoException
from Persistencia.repositorio_reportes import RepositorioReportes
from Persistencia.repositorio_partidas import RepositorioPartidas


class GestionTransacciones:
    def __init__(self, mercado: GestionMercado, inversores: GestionInversores, repo_reportes: RepositorioReportes,
                 repo_partidas: RepositorioPartidas):
        self.mercado = mercado
        self.gestor_inversores = inversores
        self.repo_reportes = repo_reportes
        self.repo_partidas = repo_partidas
        self.log_eventos = []

    def ejecutar_compra(self, id_inversor: str, ticker: str, cantidad: float) -> Transaccion:
        if cantidad <= 0:
            raise ImporteInvalidoException("La cantidad a comprar debe ser mayor a 0.")

        activo = self.mercado.obtener_activo(ticker)
        inversor = self.gestor_inversores.obtener_inversor(id_inversor)

        transaccion = Transaccion(tipo="COMPRA", ticker=ticker, cantidad=cantidad, precio_ejecucion=activo._precio_actual)
        coste_total = transaccion.obtener_monto_total()

        # --- AQUÍ ESTÁ LA MAGIA: COMPROBACIÓN DE SALDO ---
        cartera_principal = inversor._carteras[0]

        if cartera_principal._saldo < coste_total:
            # Si cuesta más de lo que tiene, lanzamos el error de tu rúbrica
            raise LimiteSuperadoException(f"Saldo insuficiente. Tienes {cartera_principal._saldo:.2f}€ y necesitas {coste_total:.2f}€.")

        # Si tiene dinero, se lo restamos y le damos las acciones
        cartera_principal.descontar_saldo(coste_total)
        cartera_principal.agregar_posicion(ticker, cantidad)
        # ------------------------------------------------

        evento = RegistroHistorial("COMPRA", f"{inversor._nombre} compró {cantidad} de {ticker}")
        self.log_eventos.append(evento)

        return transaccion

    def generar_reporte_usuario(self, id_inversor: str) -> bool:
        inversor = self.gestor_inversores.obtener_inversor(id_inversor)

        contenido = f"--- REPORTE DE INVERSOR ---\n"
        contenido += f"Nombre: {inversor._nombre}\n"
        contenido += f"Patrimonio Total: {inversor.calcular_patrimonio_total()}€\n"

        nombre_fichero = f"reporte_{id_inversor}.txt"
        return self.repo_reportes.generar_reporte(nombre_fichero, contenido)

    def guardar_partida_completa(self, nombre_fichero: str) -> bool:
        estado = {
            "mercado": self.mercado.activos_disponibles,
            "inversores": self.gestor_inversores.inversores,
            "historial": self.log_eventos
        }
        return self.repo_partidas.guardar_partida(nombre_fichero, estado)