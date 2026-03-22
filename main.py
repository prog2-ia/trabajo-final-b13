from Entidades.Bono import Bono
from Entidades.Alerta import Alerta
from Entidades.Inversor import Inversor
from Entidades.Divisa import Divisa
from Entidades.Estrategia import Estrategia
from Entidades.Etiqueta import Etiqueta
from Entidades.Transaccion import Transaccion
from Entidades.RegistroHistorial import RegistroHistorial

def demo_simplificada():
    #  Definimos la moneda y una etiqueta para clasificar activos
    moneda = Divisa("Euro", "EUR", "€")
    tag = Etiqueta("Renta Fija", "Riesgo Bajo")
    print(f">> Sistema iniciado. Divisa: {moneda} | Tag: {tag.nombre}")

    # Creamos un Bono (pertenece a los activos)
    b1 = Bono("Bono España 5Y", "ES5Y", 102.50, 2.5, "2029-05-12")
    print(f"Activo cargado: {b1}")

    # Creamos una estrategia y una alerta de seguridad
    est = Estrategia("Ahorro Seguro")
    est.definir_peso("ES5Y", 1.0)

    alerta = Alerta("ES5Y", 100.00, "BAJADA")
    print(f"Estrategia '{est._nombre}' activa. Umbral alerta: {alerta._precio_umbral}{moneda.simbolo}")

    # El inversor realiza una compra
    tx = Transaccion("COMPRA", "ES5Y", 20, 102.50)
    print(f"Ejecutando TX... Total: {tx.obtener_monto_total()}{moneda.simbolo}")

    #  Guardamos lo ocurrido en el historial
    historial = RegistroHistorial("ORDEN_EJECUTADA", "Compra de 20 bonos realizada con éxito")
    print(f"LOG: {historial}")

    # Mostramos quién es el inversor final
    user = Inversor("Oscar Marco", "USR-001")
    print(f"Inversor responsable: {user._nombre}")

if __name__ == "__main__":
    print("--- DEBUG ENTIDADES ---")
    demo_simplificada()