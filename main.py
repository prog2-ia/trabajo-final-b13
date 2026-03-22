from Entidades.Bono import Bono
from Entidades.Alerta import Alerta
from Entidades.Inversor import Inversor
from Entidades.Divisa import Divisa
from Entidades.Estrategia import Estrategia
from Entidades.Etiqueta import Etiqueta
from Entidades.Transaccion import Transaccion
from Entidades.RegistroHistorial import RegistroHistorial

def ejecutar_demo_entidades():
    #  Definimos la moneda y una etiqueta para clasificar activos
    divisa_eur = Divisa("Euro", "EUR", "€")
    tag_riesgo = Etiqueta("Renta Fija", "Riesgo Bajo")
    print(f"SISTEMA: {divisa_eur} | TAG: {tag_riesgo.nombre}")

    # Creamos un Bono y chequeamos su riesgo
    bono_es = Bono("Bono España 5Y", "ES5Y", 102.50, 2.5, "2029-05-12")
    riesgo_bono = bono_es.calcular_riesgo()
    print(f"ACTIVO: {bono_es} | RIESGO: {riesgo_bono}")

    # Creamos una estrategia y validamos si los pesos son correctos
    estrategia_inv = Estrategia("Ahorro Seguro")
    estrategia_inv.definir_peso("ES5Y", 1.0)
    estado_plan = "VÁLIDA" if estrategia_inv.es_valida() else "INVÁLIDA"
    print(f"PLAN: '{estrategia_inv._nombre}' | ESTADO: {estado_plan}")

    # Seteamos una alerta y probamos si saltaría con un precio nuevo
    alerta_precio = Alerta("ES5Y", 100.00, "BAJADA")
    precio_mercado = 99.50
    aviso = "¡DISPARADA!" if alerta_precio.verificar(precio_mercado) else "No activa"
    print(f"ALERTA: Umbral {alerta_precio._precio_umbral}{divisa_eur.simbolo} | TEST a {precio_mercado}: {aviso}")

    # El inversor realiza una compra y calculamos el monto
    compra_tx = Transaccion("COMPRA", "ES5Y", 20, 102.50)
    total = compra_tx.obtener_monto_total()
    print(f"TX: {compra_tx._tipo} de {compra_tx._ticker} | TOTAL: {total}{divisa_eur.simbolo}")

    #  Guardamos lo ocurrido en el historial
    log_historial = RegistroHistorial("ORDEN_EJECUTADA", f"Compra de 20 unidades de {compra_tx._ticker}")
    print(f"HISTORIAL: {log_historial}")

    # Mostramos quién es el inversor final
    inversor_usr = Inversor("Oscar Marco", "USR-001")
    print(f"USUARIO: {inversor_usr._nombre} (ID: {inversor_usr._id_usuario})")

if __name__ == "__main__":
    print("--- INICIANDO TEST DE ENTIDADES ---")
    ejecutar_demo_entidades()