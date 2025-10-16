# Nochevieja 🌃

Calcular los minutos que faltan para la medianoche a partir de una hora dada en formato HH:MM.

---

## 1. Contexto

Este ejercicio sigue una metodología donde el docente proporciona la estructura principal del programa y los tests de verificación. El alumno solo debe centrarse en implementar la función con la lógica principal del problema.

---

## 2. Enunciado

Ramón se pasa el día de Nochevieja contando los minutos que faltan para que den las uvas. Debes escribir un programa que, para una hora dada, calcule cuántos minutos quedan hasta la medianoche (24:00).

El programa procesará múltiples casos de prueba. Cada caso es una hora en una línea.

La entrada termina cuando la hora es `00:00`, la cual no se procesa.

---

## 3. Datos de Entrada

Varias líneas, cada una con una hora en formato `HH:MM` (dos dígitos para hora y dos para minutos).

La entrada finaliza con la línea `00:00`.

---

## 4. Datos de Salida

Para cada caso de prueba, se mostrará una línea con el número entero de minutos que faltan para medianoche.

---

## 5. Ejemplo de Entrada

```
23:45
21:30
00:01
00:00
```

---

## 6. Ejemplo de Salida

```
15
150
1439
```

---

## 7. Tarea del Alumnado

La lectura de líneas desde un fichero y el bucle principal ya están resueltos por el docente en el fichero `programa.py`.

Debes implementar únicamente la función `procesar_linea` en el fichero `solucion.py`.

### Firma esperada (en Python):

```python
def procesar_linea(linea: str) -> int:
    """
    Recibe: una cadena con la hora en formato "HH:MM".
    Devuelve: el número total de minutos que faltan hasta la medianoche.
    """
```

### Pautas

- No uses librerías de fechas: el objetivo es resolverlo con matemáticas simples.
- Usa el método `split(':')` para separar la cadena de la hora en dos partes: horas y minutos.
- Convierte ambas partes a tipo `int` para poder operar con ellas.
- Calcula los minutos totales que han transcurrido desde las 00:00:

```python
minutos_transcurridos = horas * 60 + minutos
```

- Un día completo tiene `24 * 60 = 1440` minutos. Resta los minutos transcurridos a este total para obtener los minutos restantes.
- Devuelve el resultado como un número entero.

---

## 8. Verificación

El docente proporciona un fichero `test_nochevieja.py` con un conjunto de tests de `pytest` para verificar que tu función `procesar_linea` es correcta.

Para ejecutar los tests, abre una terminal en la carpeta del proyecto y ejecuta los siguientes comandos:

```bash
# Instalar pytest si no lo tienes
pip install -U pytest

# Ejecutar los tests
pytest -q
```