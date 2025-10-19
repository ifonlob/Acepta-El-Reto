'''# Código de Barras (Acepta el reto 106)

Este proyecto resuelve el problema de validación de códigos de barras EAN-8 y EAN-13, siguiendo el formato y requisitos del juez de aceptaelreto.com.

## Descripción

El programa recibe una lista de códigos de barras en formato texto (uno por línea) e indica para cada uno si cumple con el dígito de control estándar. Para los códigos EAN-13 válidos, muestra también el país correspondiente según una tabla estándar, o "Desconocido" si no está en la tabla.

### Formato de salida
- **EAN-8** válido: `SI`
- **EAN-8** inválido: `NO`
- **EAN-13** válido y país en tabla: `SI <PAÍS>`
- **EAN-13** válido pero país no listado: `SI Desconocido`
- **EAN-13** inválido: `NO`

## Estructura de archivos
- **codigo_de_barras.py**: contiene la lógica principal y la función `procesar_linea`.
- **test_codigo_de_barras.py**: incluye tests automáticos usando pytest con los ejemplos oficiales y más casos.
- (Opcional) fichero de entrada: cada línea es un código (sin espacios), terminado por una línea `0`.

## Ejecución
### Requisitos
- Python 3.8+
- pytest (opcional, para correr los tests)

### Uso en consola
```bash
python codigo_de_barras.py <ruta_entrada.txt>
```

Donde `<ruta_entrada.txt>` es el archivo de casos. La salida se muestra por pantalla, una línea por caso.

### Test unitarios
Para lanzar los tests automáticos:
```bash
pytest test_codigo_de_barras.py
```

## Ejemplo de entrada
```
65839522
65839521
8414533043847
5029365779425
5129365779425
0
```

## Ejemplo de salida
```
SI
NO
SI Desconocido
SI Inglaterra
NO
```

## Licencia
Uso educativo y libre.
'''
