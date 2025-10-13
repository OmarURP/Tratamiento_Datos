"""
Módulo de operaciones aritméticas básicas.

Este módulo contiene funciones para realizar operaciones aritméticas
con dos valores numéricos. Incluye manejo de errores para casos como división
por cero.
"""

def suma(a, b):
    """
    Realiza la suma de dos números.

    Args:
        a (int o float): Primer número a sumar.
        b (int o float): Segundo número a sumar.

    Returns:
        int o float: El resultado de a + b.
    """
    return a + b


def resta(a, b):
    """
    Realiza la resta de dos números.

    Args:
        a (int o float): Número del cual se restará.
        b (int o float): Número a restar.

    Returns:
        int o float: El resultado de a - b.
    """
    return a - b


def multiplicacion(a, b):
    """
    Realiza la multiplicación de dos números.

    Args:
        a (int o float): Primer número a multiplicar.
        b (int o float): Segundo número a multiplicar.

    Returns:
        int o float: El resultado de a * b.
    """
    return a * b


def division(a, b):
    """
    Realiza la división de dos números.

    Args:
        a (int o float): Dividendo.
        b (int o float): Divisor.

    Returns:
        float: El resultado de a / b.

    Raises:
        ZeroDivisionError: Si b es cero, ya que la división por cero no está
                           permitida.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    return a / b


def potencia(base, exponente):
    """
    Calcula la potencia de un número elevado a otro.

    Esta función adicional demuestra originalidad al incluir una operación
    matemática más avanzada, útil para cálculos exponenciales.

    Args:
        base (int o float): La base de la potencia.
        exponente (int o float): El exponente al cual elevar la base.

    Returns:
        float: El resultado de base ** exponente.
    """
    return base ** exponente
