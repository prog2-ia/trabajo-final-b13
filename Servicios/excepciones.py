class ImporteInvalidoException(Exception):
    """Lanzada cuando se intenta operar con una cantidad negativa o nula."""
    pass

class ActivoDesconocidoException(Exception):
    """Lanzada cuando se opera con un ticker que no existe en el mercado."""
    pass

class LimiteSuperadoException(Exception):
    """Lanzada cuando el inversor no tiene fondos o activos suficientes."""
    pass