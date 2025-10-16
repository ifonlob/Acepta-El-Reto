import pytest
# Importamos la función que el alumno debe implementar desde "pipipi.py"
from pipipi import procesar_linea

@pytest.mark.parametrize(
    "linea, esperado",
    [
        # Casos del enunciado:
        ("1 1", "0:00:02:24"),
        ("3 9", "0:01:04:48"),
        ("300 2", "1:00:00:00"),

        # Casos calculados para obtener resultados exactos:
        ("5 5", "0:01:00:00"),       # El total es exactamente 1 hora (3600s)
        ("1 25", "0:01:00:00"),      # Otra combinación para 1 hora
        ("10 60", "1:00:00:00"),     # El total es exactamente 1 día (86400s)

        # Casos con valores más pequeños:
        ("1 2", "0:00:04:48"),       # Menos de 5 minutos
        ("2 2", "0:00:09:36"),       # Menos de 10 minutos

        # Casos con números grandes (dentro de los límites):
        ("1000 1", "1:16:00:00"),    # Límite de 1000 días
        ("1 1000", "1:16:00:00"),    # Número grande de emisoras
        ("500 10", "8:08:00:00"),    # Combinación de números grandes

        # Casos borde con ceros:
        ("1 0", "0:00:00:00"),       # Cero emisoras
        ("0 1", "0:00:00:00"),       # Cero días

        # Un caso que genera todos los campos (D, HH, MM, SS):
        # 1 día, 13 emisoras -> 1*13*24*6 = 1872s = 31m 12s
        ("1 13", "0:00:31:12"),
        # 40 días, 40 emisoras -> 40*40*24*6 = 230400s = 2d 16h 0m 0s
        ("40 40", "2:16:00:00"),
    ]
)
def test_procesar_linea(linea, esperado):
    """
    Esta función de test llama a la función del alumno 'procesar_linea'
    y comprueba que el resultado que devuelve es igual al 'esperado'.
    """
    assert procesar_linea(linea) == esperado