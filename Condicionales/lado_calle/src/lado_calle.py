from typing import List
import sys
from pathlib import Path

def leer_casos(ruta_fichero: str) -> List[str]:
    """
    Lee un fichero de texto con casos de prueba, devolviendo
    una lista de líneas (str) ya limpias, sin la línea de terminación "0 0 0".
    Ignora líneas en blanco y comentarios que empiecen por '#'.
    """
    ruta = Path(ruta_fichero)
    if not ruta.exists():
        raise FileNotFoundError(f"No existe el fichero: {ruta_fichero}")

    casos: List[str] = []
    with ruta.open(encoding="utf-8") as f:
        for raw in f:
            linea = raw.strip()
            if not linea or linea.startswith("#"):
                continue
            if linea == "0 0 0":
                break
            casos.append(linea)
    return casos


def procesar_linea(linea: str) -> str:
    """
    TODO: Implementar por el alumnado.

    Recibe:
        linea (str): una cadena que contiene el número de una vivienda.

    Debe devolver:
        (str): "IZQUIERDA" si el número es impar, o "DERECHA" si el número es par.
    """
    numero_vivienda = linea
    try:
       numero_vivienda = int(numero_vivienda)
    except ValueError:
        return "ERROR"
    if numero_vivienda % 2 == 0:
        return "DERECHA"
    else:
        return "IZQUIERDA" 
def main(argv: List[str]) -> None:
    if len(argv) < 2:
        print("Uso: python programa.py <ruta_entrada.txt>")
        sys.exit(1)

    ruta = argv[1]
    for linea in leer_casos(ruta):
        resultado = procesar_linea(linea)
        print(resultado)
if __name__ == "__main__":
    main(sys.argv)