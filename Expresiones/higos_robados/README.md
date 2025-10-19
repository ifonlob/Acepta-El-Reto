
# Higos robados

## Descripción

Este ejercicio está basado en el problema "Higos robados" de la plataforma [Acepta el reto](https://aceptaelreto.com). Manola y su grupo de amigos se reparten los higos recolectados de manera equitativa, y Manola se queda con el resto si no hay reparto exacto.

## Enunciado

La entrada comienza con un número que indica cuántos casos de prueba hay. Cada caso se compone de dos números: (personas en la pandilla, número total de higos recolectados).

La salida es el número de higos que corresponderá a Manola tras el reparto.

### Ejemplo

#### Entrada
```
3
4 4
4 5
5 13
```

#### Salida
```
1
2
5
```

## Implementación
La función principal que debe implementarse es:

```python
def procesar_linea(personas: int, higos: int) -> int:
    """
    Calcula el número de higos que recibe Manola tras el reparto.
    """
```

## Tests automáticos

El archivo `test_higos_robados.py` contiene los casos de ejemplo y adicionales para comprobar el correcto funcionamiento mediante [pytest](https://pytest.org).

Para ejecutar los tests:

```bash
pytest -v
```

## Requisitos
- Python >= 3.7
- pytest

Instala pytest si no lo tienes:
```bash
pip install pytest
```

## Créditos
Ejercicio de la plataforma Acepta el Reto adaptado para la práctica de programación básica y algoritmos.
