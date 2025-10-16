# test_nochevieja.py
# -*- coding: utf-8 -*-

import pytest
from nochevieja import procesar_linea
import sys

@pytest.mark.parametrize(
    "linea, esperado",
    [
        # Casos del enunciado:
        ("23:45", 15),
        ("21:30", 150),
        ("00:01", 1439),

        # Bordes y sanity checks:
        ("23:59", 1),      # El último minuto del día
        ("12:00", 720),    # Justo a mediodía
        ("08:00", 960),    # Una hora en punto de la mañana (16h restantes)
        ("15:15", 525),    # Una hora con minutos por la tarde
        ("01:00", 1380),   # La primera hora tras la medianoche
        ("00:59", 1381),   # La primera hora sin llegar a ser en punto
    ]
)
def test_procesar_linea(linea, esperado):
    """
    Esta función de test llama a la función del alumno 'procesar_linea'
    y comprueba que el resultado que devuelve es igual al 'esperado'.
    """
    assert procesar_linea(linea) == esperado
