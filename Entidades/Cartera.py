class Cartera:
    """
    Representa la cartera de un inversor, almacenando su saldo y activos.
    """

    def __init__(self, nombre: str, saldo_inicial: float = 0.0):
        self._nombre = nombre
        self._saldo = saldo_inicial
        self._posiciones = {}  # Formato: {ticker: cantidad}

    # -- Sobrecarga de operadores --

    def __add__(self, otra_cartera: 'Cartera') -> 'Cartera':
        """Permite sumar dos carteras usando el operador '+'."""
        nuevo_nombre = f"{self._nombre} + {otra_cartera._nombre}"
        nueva_cartera = Cartera(nuevo_nombre, self._saldo + otra_cartera._saldo)

        for ticker, cantidad in self._posiciones.items():
            nueva_cartera.agregar_posicion(ticker, cantidad)

        for ticker, cantidad in otra_cartera._posiciones.items():
            nueva_cartera.agregar_posicion(ticker, cantidad)

        return nueva_cartera

    def __gt__(self, otra_cartera: 'Cartera') -> bool:
        """Permite comparar si una cartera tiene más saldo que otra usando '>'."""
        return self._saldo > otra_cartera._saldo

    # -- Métodos de gestión --

    def agregar_posicion(self, ticker: str, cantidad: float) -> None:
        if ticker in self._posiciones:
            self._posiciones[ticker] += cantidad
        else:
            self._posiciones[ticker] = cantidad

    def descontar_saldo(self, cantidad: float) -> None:
        self._saldo -= cantidad

    def valor_total(self) -> float:
        # Aquí idealmente multiplicarías las posiciones por el precio actual del mercado
        return self._saldo

    def __str__(self) -> str:
        return f"Cartera '{self._nombre}' | Saldo: {self._saldo:.2f}€"