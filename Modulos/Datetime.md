# Datetime

**Datetime** es un módulo incorporado en la biblioteca estándar de Python que proporciona clases para manipular fechas y horas. Ofrece soporte para realizar operaciones aritméticas con fechas, formatear datos temporales en cadenas de texto y convertir texto en objetos de fecha, permitiendo además el manejo de husos horarios (zonas horarias).

## Principales Clases en Datetime

El módulo organiza sus funcionalidades a través de varias clases fundamentales:

1. **`date`:** Representa una fecha idealizada (año, mes y día) según el calendario gregoriano actual.
2. **`time`:** Representa una hora idealizada (hora, minuto, segundo, microsegundo), independiente de cualquier fecha particular.
3. **`datetime`:** Combina los atributos de las clases `date` y `time` (año, mes, día, hora, minuto, segundo, microsegundo).
4. **`timedelta`:** Representa una duración o diferencia entre dos fechas o tiempos, útil para realizar cálculos matemáticos temporales.
5. **`timezone`:** Implementa la información sobre zonas horarias y desfases con respecto a UTC.

---

## Ejemplos de uso de Datetime

A continuación se presentan ejemplos que detallan las operaciones más usuales al trabajar con marcas temporales.

### 1. Obtener la fecha y hora actuales

Es posible instanciar objetos que capturen la información del reloj del sistema.

```python
from datetime import datetime, date

# Se obtiene la fecha y hora actuales del sistema
fecha_hora_actual = datetime.now()
print("Fecha y hora actuales:", fecha_hora_actual)

# Se obtiene únicamente la fecha de hoy
hoy = date.today()
print("Fecha de hoy (solo año-mes-día):", hoy)

# Se accede a los componentes individuales de la fecha actual
print(f"Año: {fecha_hora_actual.year}, Mes: {fecha_hora_actual.month}, Día: {fecha_hora_actual.day}")
```

### 2. Formatear fechas a cadenas de texto (`strftime`)

Para representar las fechas en formatos legibles según la región o necesidad, se utiliza el método `strftime` (String Format Time).

```python
from datetime import datetime

ahora = datetime.now()

# Formato estándar de base de datos (YYYY-MM-DD HH:MM:SS)
formato_bd = ahora.strftime("%Y-%m-%d %H:%M:%S")
print("Formato de base de datos:", formato_bd)

# Formato personalizado legible en español (DD/MM/YYYY)
formato_espanol = ahora.strftime("%d/%m/%Y")
print("Formato en español:", formato_espanol)

# Formato detallado de hora y periodo (HH:MM AM/PM)
formato_hora = ahora.strftime("%I:%M %p")
print("Hora formateada:", formato_hora)
```

### 3. Convertir texto en objetos de fecha (`strptime`)

Cuando se leen fechas desde archivos de texto o entradas de usuario en formato de texto, se emplea el método `strptime` (String Parse Time) para reconstruir el objeto.

```python
from datetime import datetime

fecha_texto = "2026-10-15 14:30:00"

# Se procesa la cadena indicando el formato exacto en el que viene estructurada
objeto_fecha = datetime.strptime(fecha_texto, "%Y-%m-%d %H:%M:%S")

print("Objeto datetime reconstruido:", objeto_fecha)
print("Tipo de objeto creado:", type(objeto_fecha))
```

### 4. Operaciones aritméticas y diferencias temporales (`timedelta`)

La clase `timedelta` permite sumar o restar lapsos de tiempo a un objeto existente, así como calcular el tiempo transcurrido entre dos eventos.

```python
from datetime import datetime, timedelta

ahora = datetime.now()

# Se define un intervalo de tiempo (por ejemplo, 10 días y 5 horas)
intervalo = timedelta(days=10, hours=5)

# Se calcula una fecha futura sumando el intervalo
fecha_futura = ahora + intervalo
print("Fecha dentro de 10 días y 5 horas:", fecha_futura)

# Se calcula una fecha pasada restando el intervalo
fecha_pasada = ahora - intervalo
print("Fecha hace 10 días y 5 horas:", fecha_pasada)

# Cálculo de la diferencia entre dos fechas
navidad_2026 = datetime(2026, 12, 25)
diferencia = navidad_2026 - ahora
print(f"Días restantes para Navidad de 2026: {diferencia.days} días")
```
