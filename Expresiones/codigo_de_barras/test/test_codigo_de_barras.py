import pytest
from codigo_de_barras import procesar_linea

@pytest.mark.parametrize(
    "linea, esperado",
    [
        # --- Ejemplos Oficiales (Válidos) ---
        ("65839522", "SI"),
        ("65839521", "NO"),
        ("8414533043847", "SI Desconocido"),
        ("5029365779425", "SI Inglaterra"),
        ("5129365779425", "NO"), 

        # --- EAN-8 adicionales (Válidos) ---
        ("12345670", "SI"),
        ("12345671", "NO"),
        ("00000000", "SI"),
        ("12345", "NO"), # Rellena a 00012345, Control debe ser 8

        # --- EAN-13 VÁLIDOS con país (RE-CALCULADOS) ---
        ("3801234567898", "SI Bulgaria"),   # Control = 8
        ("5391234567892", "SI Irlanda"),    # Control = 2
        ("5601234567892", "SI Portugal"),   # Control = 2
        ("8901234567890", "SI India"),      # Control = 0
        ("8501234567892", "SI Cuba"),       # Control = 2
        ("7591234567894", "SI Venezuela"),  # Control = 4
        ("7012345678908", "SI Noruega"),    # Control = 8
        ("5012345678900", "SI Inglaterra"), # Control = 0
        ("0123456789012", "SI EEUU"),       # Control = 2

        # --- EAN-13 válidos con país desconocido ---
        ("1234567890128", "SI Desconocido"), # Control = 8
    ]
)

def test_procesar_linea(linea, esperado):
    """
    Test parametrizado para 'Código de barras' (Acepta el reto 106):
    Valida casos oficiales, de la tabla y desconocidos, tanto EAN-8 como EAN-13.
    """
    assert procesar_linea(linea) == esperado
