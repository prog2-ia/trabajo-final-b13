import os
from Servicios.gestion_transacciones import GestionTransacciones
from Servicios.excepciones import (
    ImporteInvalidoException,
    ActivoDesconocidoException,
    LimiteSuperadoException
)

# Definimos los colores para la terminal
VERDE = '\033[92m'
ROJO = '\033[91m'
AMARILLO = '\033[93m'
RESET = '\033[0m'


class InterfazConsola:
    def __init__(self, gestor_t: GestionTransacciones):
        self.gestor_t = gestor_t

    def _limpiar_pantalla(self):
        # Detecta si es Windows (nt) o Mac/Linux para usar el comando correcto
        os.system('cls' if os.name == 'nt' else 'clear')

    def ejecutar_menu(self):
        while True:
            self._limpiar_pantalla()
            print(f"{AMARILLO}--- Simulador de Bolsa ---{RESET}")
            print("1. Comprar activo")
            print("2. Generar reporte de inversor")
            print("3. Guardar partida")
            print("4. Salir")

            opcion = input("\nElige una opción: ")

            if opcion == "1":
                self._menu_compra()
            elif opcion == "2":
                self._menu_reporte()
            elif opcion == "3":
                self._menu_guardar()
            elif opcion == "4":
                self._limpiar_pantalla()
                print("Cerrando el simulador...")
                break
            else:
                print(f"{ROJO}Opción incorrecta, prueba otra vez.{RESET}")
                input("\nPulsa Enter para continuar...")

    def _menu_compra(self):
        self._limpiar_pantalla()
        print(f"{AMARILLO}-- Comprar Activo --{RESET}")
        id_inv = input("ID del inversor: ")
        ticker = input("Ticker (ej. AAPL): ").upper()

        # Bucle de validación a prueba de balas para la cantidad
        while True:
            try:
                cantidad = float(input("Cantidad a comprar: "))
                break  # Si mete un número correcto, rompemos el bucle y seguimos
            except ValueError:
                print(f"{ROJO}Error: Tienes que introducir un número válido (ej: 2 o 2.5).{RESET}")

        try:
            transaccion = self.gestor_t.ejecutar_compra(id_inv, ticker, cantidad)
            coste = transaccion.obtener_monto_total()
            print(f"{VERDE}Operación completada. Coste total: {coste:.2f}€{RESET}")

        except (ImporteInvalidoException, ActivoDesconocidoException, LimiteSuperadoException) as e:
            print(f"{ROJO}Error en la operación: {e}{RESET}")
        except Exception as e:
            print(f"{ROJO}Error del sistema: {e}{RESET}")

        input("\nPulsa Enter para volver al menú...")

    def _menu_reporte(self):
        self._limpiar_pantalla()
        print(f"{AMARILLO}-- Generar Reporte --{RESET}")
        id_inv = input("ID del inversor: ")
        try:
            if self.gestor_t.generar_reporte_usuario(id_inv):
                print(f"{VERDE}Reporte generado en data/reporte_{id_inv}.txt{RESET}")
        except Exception as e:
            print(f"{ROJO}Error al generar el reporte: {e}{RESET}")

        input("\nPulsa Enter para volver al menú...")

    def _menu_guardar(self):
        self._limpiar_pantalla()
        print(f"{AMARILLO}-- Guardar Partida --{RESET}")
        try:
            if self.gestor_t.guardar_partida_completa("partida_actual.pkl"):
                print(f"{VERDE}Partida guardada correctamente.{RESET}")
        except Exception as e:
            print(f"{ROJO}Error al guardar: {e}{RESET}")

        input("\nPulsa Enter para volver al menú...")