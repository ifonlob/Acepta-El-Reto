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
    Procesa una línea de entrada correspondiente al problema 'Código de barras' (Acepta el reto 106).

    Parámetros:
        linea (str): Cadena representando un código de barras EAN-8 o EAN-13.
    
    Devuelve:
        str: Una cadena con el resultado de validación:
            - "SI" si el dígito de control es correcto (EAN-8).
            - "SI <PAÍS>" si es EAN-13 válido y el código de país está en la tabla.
            - "Desconocido" si el país no aparece en la tabla.
            - "NO" si el dígito de control no es correcto.
    
    Detalles:
        Esta función debe validar el dígito de control según las reglas de los estándares EAN-8 y EAN-13.
        Si la longitud del código es inferior a 8, se asume EAN-8 (completando con ceros a la izquierda);
        si es superior a 8 pero inferior a 13, se asume EAN-13 (completando igualmente con ceros).
        
        En el caso de que el código EAN-13 sea correcto, se busca el país
        según la tabla incluida en el enunciado del problema. Si no se encuentra, se devuelve "Desconocido".

    TODO:
        Implementar la lógica completa de validación del dígito de control y detección de país.
    """
    codigo_barras = linea.strip()
    if not codigo_barras.isdigit():
        return "NO"
    multiplicador = 0
    i = 0
    if len(codigo_barras) <= 8:
        acumulador = 0
        codigo_barras = codigo_barras.zfill(8)
        codigo_barras = list(codigo_barras)
        for i in range(0,len(codigo_barras)-1):
            if i % 2 == 0:
                multiplicador = 3
                acumulador = acumulador + int(codigo_barras[i])*multiplicador
            else:
                acumulador = acumulador + int(codigo_barras[i])
        digito_comprobacion = codigo_barras[7]
        digito_comprobacion = int(digito_comprobacion)
        digito_control = (10 - (acumulador % 10)) % 10
        if digito_comprobacion == digito_control:
            return "SI"
        else:
            return "NO"       
    elif len(codigo_barras) <= 13:
        acumulador = 0
        codigo_barras = codigo_barras.zfill(13)
        codigo_barras = list(codigo_barras)
        for i in range(0, len(codigo_barras) - 1):
            pos_desde_derecha = (len(codigo_barras) - 1) - i
            if pos_desde_derecha % 2 == 1:
                multiplicador = 3
            else:
                multiplicador = 1
            acumulador = acumulador + int(codigo_barras[i]) * multiplicador
        digito_comprobacion = int(codigo_barras[12])
        digito_control = (10 - (acumulador % 10)) % 10
        if digito_comprobacion == digito_control:
            diccionario_paises = {
                "0": "EEUU",
                "380": "Bulgaria",
                "50": "Inglaterra",
                "539": "Irlanda",
                "560": "Portugal",
                "70": "Noruega",
                "759": "Venezuela",
                "850": "Cuba",
                "890": "India",
            } 
            for j in (3, 2, 1):
                identificador_pais = "".join(codigo_barras[:j])
                if identificador_pais in diccionario_paises:
                    return f"SI {diccionario_paises[identificador_pais]}"
            return "SI Desconocido"
        else:
            return "NO"
    else:
        return "NO"
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