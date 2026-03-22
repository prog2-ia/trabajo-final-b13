
# Importamos todas tus entidades
# Cambia tus imports en main.py por estos:
from Entidades.Activo import Activo
from Entidades.Bono import Bono
from Entidades.Alerta import Alerta
from Entidades.Inversor import Inversor
from Entidades.Divisa import Divisa
from Entidades.Estrategia import Estrategia
from Entidades.Etiqueta import Etiqueta
from Entidades.Transaccion import Transaccion
from Entidades.RegistroHistorial import RegistroHistorial
from datetime import datetime
def demo_total():
    print("=== SISTEMA DE INVERSIONES ===")

    # 1. Configuración básica (Etiqueta y Divisa)
    etiqueta_bono = Etiqueta("Renta Fija", "Categoría")
    eur = Divisa("Euro", "EUR", "€")
    print(f"Configurando entorno en {eur} con etiquetas de {etiqueta_bono.nombre}")

    # 2. Definir el Activo (Bono)
    # IMPORTANTE: Para que funcione, Bono debe tener implementado 'actualizar_precio'
    mi_bono = Bono("Bono Estado 10Y", "B10Y", 98.20, 3.25, "2034-01-01")
    print(f"Activo creado: {mi_bono}")

    # 3. Estrategia y Alerta
    estrategia_conservadora = Estrategia("Conservadora")
    estrategia_conservadora.definir_peso("B10Y", 1.0)  # 100% de la cartera a este bono

    alerta_precio = Alerta("B10Y", 95.00, "BAJADA")
    print(f"Estrategia '{estrategia_conservadora._nombre}' lista. Alerta de seguridad activa.")

    # 4. Operación (Transacción y Registro)
    compra = Transaccion("COMPRA", "B10Y", 50, 98.20)
    log = RegistroHistorial("OPERACION", f"Compra de {compra._cantidad} unidades de {compra._ticker}")
    print(f"Transacción realizada: Total {compra.obtener_monto_total()}{eur.simbolo}")
    print(f"Log: {log}")

    # 5. El Inversor
    inversor = Inversor("Oscar Marco", "USR-404")
    print(f"Inversor {inversor._nombre} creado exitosamente.")

    # Verificación de lógica de alerta
    precio_caida = 94.50
    if alerta_precio.verificar(precio_caida):
        print(f"¡AVISO! El precio cayó a {precio_caida}. Alerta de {alerta_precio._tipo_alerta} disparada.")


if __name__ == "__main__":
    demo_total()