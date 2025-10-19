# La abuela María

## Descripción

Este ejercicio pertenece a la plataforma [Acepta el Reto](https://aceptaelreto.com) y consiste en determinar, para cada día, si los dientes superiores de la abuela María encajan perfectamente con los inferiores, formando una sonrisa sin huecos. La entrada consiste en configuraciones diarias de los dientes y la salida indica si encajan o no.

## Enunciado

Para cada caso de prueba, se reciben dos líneas con las alturas de los 6 dientes superiores y los 6 dientes inferiores responsables de la sonrisa (de izquierda a derecha). Todos son números enteros entre 0 y 2000.

Se debe escribir "SI" si los dientes encajan perfectamente sin dejar huecos, o "NO" en caso contrario.

Un caso encaja perfectamente si, para todos los pares de dientes, la suma de la altura superior e inferior en cada posición es la misma para todas las posiciones.

### Ejemplo

#### Entrada

```
2
1 3 1 3 1 3
3 1 3 1 3 1
1 1 1 1 1 1
1 2 1 1 1 1
```

#### Salida

```
SI
NO
```

## Implementación

La función principal es:

```python
def procesar_linea(sup: list[int], inf: list[int]) -> str:
    """
    Determina si los dientes superiores encajan perfectamente con los inferiores en la sonrisa de la abuela María.

    Args:
        sup (list[int]): Alturas de los 6 dientes superiores.
        inf (list[int]): Alturas de los 6 dientes inferiores.

    Returns:
        str: 'SI' si encajan perfectamente, 'NO' en caso contrario.
    """
```

## Tests automáticos

El archivo `test_abuela_maria.py` contiene varios casos de prueba para verificar tu implementación con [pytest](https://pytest.org).

Para ejecutar los tests:

```bash
pytest -v
```

Verás el detalle de los casos que pasan y los que fallan.

## Requisitos

- Python >= 3.7
- pytest

Instala pytest si no lo tienes:

```bash
pip install pytest
```

## Créditos

Ejercicio perteneciente al repositorio Acepta el Reto.  
Documentación y tests adaptados para práctica de programación y algoritmos básicos.
'''