import pytest
from higos_robados import procesar_linea
@pytest.mark.parametrize(
    "personas, higos, esperado",
    [
        (4, 4, 1),   # Todas pueden llevarse 1 higo, Manola se queda 1
        (4, 5, 2),   # Cada uno 1 y Manola se queda 2
        (5, 13, 5),  # Cada uno 2 y Manola se queda 5
        (2, 3, 2),   # Un compañero y Manola, se reparten 1 cada uno y Manola, 2
        (10, 100, 10), # Reparto exacto
        (10, 123, 15), # Resto muy grande
        (1, 17, 17),   # Solo Manola, se queda todos
    ]
)
def test_procesar_linea(personas, higos, esperado):
    assert procesar_linea(personas, higos) == esperado