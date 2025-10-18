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
        linea (str): una cadena con dos números enteros separados por un espacio:
                     el número de días y el número de emisoras.

    Debe devolver:
        (str): una cadena con el tiempo total acumulado en formato "D:HH:MM:SS".
               HH, MM, y SS deben tener siempre dos dígitos (rellenando con un
               cero a la izquierda si es necesario).
    """
    dias,emisoras = linea.split()
    try:
        dias = int(dias)
        emisoras = int(emisoras)
    except ValueError:
        return "ERROR" 
    # 2. Calcular el total de segundos de forma correcta
    total_segundos = dias * emisoras * 144
    # 3. Usar división entera (//) y módulo (%) para descomponer el tiempo
    # Segundos que quedan después de agrupar en minutos
    resto_segundos = total_segundos % 60
    minutos_totales = total_segundos // 60
    # Minutos que quedan después de agrupar en horas
    resto_minutos = minutos_totales % 60
    horas_totales = minutos_totales // 60
    # Horas que quedan después de agrupar en días
    resto_horas = horas_totales % 24
    d = horas_totales // 24
    return f"{d}:{resto_horas:02d}:{resto_minutos:02d}:{resto_segundos:02d}"

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