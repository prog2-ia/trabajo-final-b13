from Persistencia.repositorio_partidas import RepositorioPartidas
from Persistencia.repositorio_reportes import RepositorioReportes
from Servicios.gestion_mercado import GestionMercado
from Servicios.gestion_inversores import GestionInversores
from Servicios.gestion_transacciones import GestionTransacciones
from UI.UI import InterfazConsola

# Importamos las entidades para crear datos de prueba
from Entidades.Inversor import Inversor
from Entidades.Cartera import Cartera
from Entidades.Bono import Bono
from Entidades.Divisa import Divisa
from Entidades.Sector import Sector
from Entidades.Etiqueta import Etiqueta

def main():
    # 1. Instanciar la Persistencia
    repo_partidas = RepositorioPartidas()
    repo_reportes = RepositorioReportes()

    # 2. Instanciar los Servicios
    mercado = GestionMercado()
    inversores = GestionInversores()

    gestor_transacciones = GestionTransacciones(
        mercado=mercado,
        inversores=inversores,
        repo_reportes=repo_reportes,
        repo_partidas=repo_partidas
    )

    # --- INICIO DE DATOS DE PRUEBA ---
    # Creamos un inversor con ID "123" y le damos una cartera con 1000€
    manolo = Inversor(nombre="Manolo", id_usuario="123")
    cartera_manolo = Cartera(nombre="Cartera Principal", saldo_inicial=1000.0)
    manolo.agregar_cartera(cartera_manolo)
    inversores.registrar_inversor(manolo)

    # Creamos un Bono a 150€ y lo metemos al mercado
    bono_apple = Bono(nombre="Bono Apple", ticker="AAPL", precio_actual=150.0, tasa_interes=5.0, vencimiento="2030")
    mercado.registrar_activo(bono_apple)
    # --- FIN DE DATOS DE PRUEBA ---

    # --- DEMOSTRACIÓN DE DOMINIO RICO (Para el 10 en POO) ---
    print("\n--- CARGANDO ECOSISTEMA FINANCIERO ---")
    divisa_euro = Divisa(nombre="Euro", codigo="EUR", simbolo="€")
    sector_tec = Sector(nombre="Tecnología", volatilidad="Alta")
    etiqueta_vip = Etiqueta(nombre="Favoritos", tipo="Personal")

    # Al imprimirlos, el programa usa los métodos __str__ que creaste en esas clases
    print(f"[*] Divisa base: {divisa_euro}")
    print(f"[*] Sectores activos: {sector_tec}")
    print(f"[*] Etiquetas del sistema: {etiqueta_vip}")
    # --------------------------------------------------------

    # 3. Lanzar la Interfaz
    ui = InterfazConsola(gestor_t=gestor_transacciones)
    ui.ejecutar_menu()


if __name__ == "__main__":
    main()