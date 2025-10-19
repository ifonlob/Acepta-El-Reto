import pytest
from abuela_maria import procesar_linea

@pytest.mark.parametrize(
    "sup, inf, esperado",
    [
        ([1, 3, 1, 3, 1, 3], [3, 1, 3, 1, 3, 1], "SI"),
        ([1, 1, 1, 1, 1, 1], [1, 2, 1, 1, 1, 1], "NO"),
        ([2, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2], "SI"),
        ([0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], "SI"),
        ([1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1], "SI"),
        ([1, 1, 1, 1, 1, 3], [1, 1, 1, 1, 1, 1], "NO"),
        ([2, 2, 2, 2, 2, 3], [2, 2, 2, 2, 2, 1], "SI"),
    ]
)
def test_procesar_linea(sup, inf, esperado):
    assert procesar_linea(sup, inf) == esperado
