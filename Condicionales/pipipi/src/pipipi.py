from typing import List
import sys
from pathlib import Path
import math

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
    dia_str,emisoras_str = linea.split()
    try:
        dias_str = int(dias)
        emisoras_str = int(emisoras)
    except ValueError:
        return "ERROR" 
    salida = []
    segundos_totales = (144*dias)*emisoras
    if (math.trunc(segundos_totales/86400)) != 0:
        numero_dias = (segundos_totales/86400)
        if numero_dias > 1:
            return "ERROR"
        else:
            salida.append(numero_dias)       
    if (segundos_totales/3600) < 23 :
        numero_horas = math.trunc((segundos_totales/3600))
        salida.append(numero_horas)
    else:
        return "ERROR"     
    if (segundos_totales/60) < 59:
        numero_minutos,decimal_segundos = ((segundos_totales/60)).split(".")
        salida.append(numero_minutos)
        numero_segundos = decimal_segundos*60
        salida.append(numero_segundos)
    else:
        return "ERROR"
    resultado = ":".join(salida)
    return resultado
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