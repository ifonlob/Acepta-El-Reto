# 🕰️ Pi. Pi. Pi. Pi. Pi. Piiiii

---

## 🏛️ Big Ben

El primer uso de señales horarias por parte de la humanidad se pierde en la noche de los tiempos.  
El canto de un gallo o el tañido de una campana sirvieron como mecanismos primitivos para avisar de los momentos en los que realizar ciertos actos en común.

La **medición del tiempo** adquirió una importancia capital cuando se comenzó a utilizar para averiguar la longitud de un punto cualquiera de la Tierra al comparar la hora local con la de un punto de referencia conocido.  

Si bien esta solución se hizo viable por primera vez en **1760**, no fue hasta la segunda mitad del siglo XIX cuando comenzó a utilizarse ampliamente.  

En esa época se establece definitivamente el **meridiano de Greenwich** como el **meridiano cero** para todo el mundo.  
Además, se construye el famoso **Big Ben**, reloj que servía para dar la hora oficial de Londres, sincronizando así los **ferrocarriles** y el **tráfico marítimo**.

---

## 📻 Las señales horarias

Obviamente, las señales del Big Ben no eran audibles a grandes distancias.  
Para solucionarlo, en la **noche de Año Nuevo de 1924**, la **BBC** decidió retransmitir sus campanadas a todo el país.  

El éxito fue tal, que el **5 de febrero de ese mismo año** comenzaron a emitir, a todas las horas en punto, las que hoy se conocen como **Greenwich Time Signal (GTS)** —las señales de la hora de Greenwich—.  

Estas señales terminaron extendiéndose por las radios de todo el mundo tras la **Segunda Guerra Mundial**.  
Son los seis famosos *pitidos*:  
- cinco cortos en los últimos segundos de cada hora,  
- y uno largo en el primer segundo de la hora siguiente.  

Durante esos **6 segundos**, las emisoras de radio no transmiten nada más para evitar lo que los ingleses llaman *“crashing the pips”*.  

Con el paso de los años, eso ha ido acumulando cada vez más **tiempo total en silencio**.  
¿Sabes cuánto?

---

## 🧩 Entrada

El programa recibirá, por la entrada estándar, múltiples casos de prueba.  
Cada uno consiste en **dos números**:
1. El número de **días** durante los cuales se ha emitido el GTS.  
2. El número de **emisoras** que lo han hecho.  

El último caso de prueba, que **no deberá procesarse**, tendrá **0 0** en ambos valores.

---

## 📤 Salida

Para cada caso de prueba el programa escribirá una línea con el **tiempo total dedicado por las emisoras a radiar el GTS**, expresado en el formato:
D:HH:MM:SS
donde:
- `D` → número de **días** (sin ceros a la izquierda, máximo 1000)  
- `HH` → **horas** (00–23)  
- `MM` → **minutos** (00–59)  
- `SS` → **segundos** (00–59)  

Los valores de horas, minutos y segundos deben escribirse siempre con **dos dígitos**.

---

## 🧮 Ejemplo de entrada
```
1 1
3 9
300 2
0 0
```
## 📊 Ejemplo de salida
```
0:00:02:24
0:01:04:48
1:00:00:00
```