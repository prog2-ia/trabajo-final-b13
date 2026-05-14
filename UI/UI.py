from Servicios.gestion_transacciones import GestionTransacciones
from Servicios.excepciones import (
    ImporteInvalidoException,
    ActivoDesconocidoException,
    LimiteSuperadoException
)


class InterfazConsola:
    def _init_(self, gestor_t: GestionTransacciones):
        # La UI solo se comunica con el servicio
        self.gestor_t = gestor_t

    def ejecutar_menu(self):
        while True:
            print("\n--- Simulador de Bolsa ---")
            print("1. Comprar activo")
            print("2. Generar reporte de inversor")
            print("3. Guardar partida")
            print("4. Salir")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                self._menu_compra()
            elif opcion == "2":
                self._menu_reporte()
            elif opcion == "3":
                self._menu_guardar()
            elif opcion == "4":
                print("Cerrando el simulador...")
                break
            else:
                print("Opción incorrecta, prueba otra vez.")

    def _menu_compra(self):
        print("\n-- Comprar Activo --")
        id_inv = input("ID del inversor: ")
        ticker = input("Ticker (ej. AAPL): ").upper()

        try:
            # Comprobamos que meta un número y no un texto
            cantidad = float(input("Cantidad a comprar: "))

            # Pasamos los datos al servicio para que haga los cálculos
            transaccion = self.gestor_t.ejecutar_compra(id_inv, ticker, cantidad)
            coste = transaccion.obtener_monto_total()
            print(f"Operación completada. Coste total: {coste:.2f}€")

        except ValueError:
            print("Error: Tienes que introducir un número válido.")
        except (ImporteInvalidoException, ActivoDesconocidoException, LimiteSuperadoException) as e:
            # Aquí capturamos las excepciones de negocio que lanza el servicio
            print(f"Error en la operación: {e}")
        except Exception as e:
            print(f"Error del sistema: {e}")

    def _menu_reporte(self):
        print("\n-- Generar Reporte --")
        id_inv = input("ID del inversor: ")
        try:
            if self.gestor_t.generar_reporte_usuario(id_inv):
                print(f"Reporte generado en data/reporte_{id_inv}.txt")
        except Exception as e:
            print(f"Error al generar el reporte: {e}")

    def _menu_guardar(self):
        print("\n-- Guardar Partida --")
        try:
            if self.gestor_t.guardar_partida_completa("partida_actual.pkl"):
                print("Partida guardada correctamente.")
        except Exception as e:
            print(f"Error al guardar: {e}")