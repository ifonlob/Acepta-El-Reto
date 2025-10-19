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

def procesar_linea(sup: list[int], inf: list[int]) -> str:
    """
    Determina si los dientes superiores encajan perfectamente con los inferiores en la sonrisa de la abuela María.

    Args:
        sup (list[int]): Alturas de los 6 dientes superiores, de izquierda a derecha.
        inf (list[int]): Alturas de los 6 dientes inferiores, de izquierda a derecha.

    Returns:
        str: 'SI' si todos los dientes superiores encajan perfectamente con los inferiores, sin huecos; 'NO' en caso contrario.

    Un caso encaja perfectamente si ninguno de los dientes choca antes que los demás y cada par superior/inferior suma lo mismo en todas las posiciones.
    """
    sup = list(map(int,sup))
    inf = list(map(int,inf))
    if len(sup) != 6 or len(inf) != 6:
        return "NO"
    suma = sup[0] + inf[0]
    for i in range(0,6):
        if suma != (sup[i]+inf[i]):
            return "NO"
    return "SI" 
                

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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