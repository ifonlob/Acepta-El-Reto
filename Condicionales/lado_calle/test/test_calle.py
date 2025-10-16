# test_calle.py
# -*- coding: utf-8 -*-

import pytest
# Importamos la función que el alumno debe implementar desde "solucion.py"
from lado_calle import procesar_linea

@pytest.mark.parametrize(
    "linea, esperado",
    [
        # Casos del enunciado:
        ("3", "IZQUIERDA"),
        ("10", "DERECHA"),
        ("41", "IZQUIERDA"),

        # Casos borde y límites:
        ("1", "IZQUIERDA"),      # El primer número impar
        ("2", "DERECHA"),       # El primer número par
        ("999", "IZQUIERDA"),     # El número impar más alto dentro del límite
        ("1000", "DERECHA"),    # El número máximo permitido

        # Casos adicionales (números pares):
        ("88", "DERECHA"),
        ("256", "DERECHA"),
        ("500", "DERECHA"),
        ("778", "DERECHA"),

        # Casos adicionales (números impares):
        ("7", "IZQUIERDA"),
        ("55", "IZQUIERDA"),
        ("123", "IZQUIERDA"),
        ("861", "IZQUIERDA"),
        
        # Casos con ceros a la izquierda (deberían funcionar si se convierten a int)
        ("01", "IZQUIERDA"),
        ("002", "DERECHA"),
    ]
)
def test_procesar_linea(linea, esperado):
    """
    Esta función de test llama a la función del alumno 'procesar_linea'
    y comprueba que el resultado que devuelve es igual al 'esperado'.
    """
    assert procesar_linea(linea) == esperado