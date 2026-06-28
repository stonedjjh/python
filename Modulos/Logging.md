# Logging

**Logging** es un módulo incorporado en la biblioteca estándar de Python diseñado para realizar el seguimiento de eventos durante la ejecución de una aplicación. Proporciona un sistema flexible para generar mensajes de diagnóstico y registrar información en diferentes salidas, como la consola de comandos, archivos de texto o servidores remotos. Al ser un módulo estándar, no requiere instalación mediante `pip`.

## Niveles de Gravedad (Log Levels)

El módulo define cinco niveles estándar para clasificar la gravedad de los eventos registrados. A continuación se presentan en orden ascendente de prioridad:

| Nivel | Valor Numérico | Propósito |
| :--- | :--- | :--- |
| `DEBUG` | 10 | Información detallada de diagnóstico, útil durante la fase de desarrollo. |
| `INFO` | 20 | Confirmación de que el programa funciona según lo previsto. |
| `WARNING` | 30 | Indicación de que algo inesperado ocurrió o podría ocurrir en el futuro (comportamiento por defecto). |
| `ERROR` | 40 | Registro de un problema grave que impidió la ejecución de una función específica. |
| `CRITICAL` | 50 | Error sumamente grave que indica que el programa no puede continuar ejecutándose. |

---

## Ejemplos de uso de Logging

A continuación se describen las implementaciones básicas y avanzadas del módulo.

### 1. Configuración básica y registro en consola

Por defecto, el nivel mínimo configurado es `WARNING`. Para registrar niveles inferiores como `DEBUG` o `INFO`, se debe ajustar la configuración inicial mediante `basicConfig`.

```python
import logging

# Se configura el nivel mínimo a registrar
logging.basicConfig(level=logging.INFO)

# Ejemplos de registro en diferentes niveles
logging.debug("Este mensaje de depuración NO se mostrará en consola (nivel inferior a INFO).")
logging.info("Se ha iniciado la ejecución del proceso.")
logging.warning("Se detectó un uso elevado de memoria ram.")
logging.error("Ocurrió un error al procesar el registro.")
logging.critical("El sistema ha fallado críticamente.")
```

### 2. Registro en un archivo de texto

Es común almacenar los eventos en un archivo físico en el disco para su posterior análisis. Para ello, se especifica el parámetro `filename`.

```python
import logging

# Se define el archivo de destino, el nivel de registro y el modo de escritura
# El modo "w" sobrescribe el archivo en cada ejecución; "a" añade los logs al final
logging.basicConfig(
    filename="aplicacion.log",
    level=logging.DEBUG,
    filemode="w",
    encoding="utf-8"
)

# Se escriben mensajes en el archivo especificado
logging.debug("Detalle del estado interno de las variables.")
logging.info("El archivo de logs se ha inicializado correctamente.")
```

### 3. Configuración del formato del mensaje (Formatters)

Para que los mensajes contengan información valiosa como la fecha, hora, nivel de gravedad y línea de código, se utiliza el parámetro `format`.

```python
import logging

# Se configuran marcadores de posición para estructurar el mensaje
# asctime: Marca de tiempo
# name: Nombre del registrador (logger)
# levelname: Nivel de gravedad
# message: Contenido del mensaje de log
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logging.info("Mensaje estructurado con fecha y hora.")
```

### 4. Registro de Excepciones

Para facilitar la depuración, es posible registrar la traza completa del error (stack trace) dentro de un bloque `try-except` utilizando el método `exception`.

```python
import logging

logging.basicConfig(level=logging.ERROR)

try:
    # Se genera un error intencional de división por cero
    resultado = 10 / 0
except ZeroDivisionError:
    # El método logging.exception captura automáticamente la traza del error
    logging.exception("Se produjo una excepción durante la operación matemática.")
```

### 5. Configuración avanzada con Logger, Handlers y Formatters

Para proyectos medianos o grandes, se desaconseja usar `logging.basicConfig`. En su lugar, se crean objetos individuales para gestionar diferentes destinos de forma independiente (por ejemplo, mostrar advertencias en consola y almacenar errores críticos en un archivo).

```python
import logging

# 1. Se crea un objeto registrador personalizado
logger = logging.getLogger("ModuloVentas")
logger.setLevel(logging.DEBUG) # Nivel base para este logger

# 2. Se crea un manejador para escribir en archivo (solo errores y críticos)
manejador_archivo = logging.FileHandler("errores_ventas.log")
manejador_archivo.setLevel(logging.ERROR)

# 3. Se crea un manejador para mostrar en consola (todos los niveles desde DEBUG)
manejador_consola = logging.StreamHandler()
manejador_consola.setLevel(logging.DEBUG)

# 4. Se define la estructura del mensaje
formato = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
manejador_archivo.setFormatter(formato)
manejador_consola.setFormatter(formato)

# 5. Se asocian los manejadores al registrador principal
logger.addHandler(manejador_archivo)
logger.addHandler(manejador_consola)

# Prueba de emisión de logs
logger.debug("Mensaje visible solo en consola.")
logger.error("Mensaje visible tanto en consola como en el archivo de errores.")
```

---

## Manejadores (Handlers)

Los manejadores (handlers) son elementos diseñados para gestionar y enrutar los registros hacia diferentes destinos. Definen las salidas de los mensajes de registro, lo que permite controlar a dónde se dirigen los datos, ya sea para guardarlos en archivos, mostrarlos en la consola, enviarlos por correo electrónico o transmitirlos a través de la red.

El manejador más básico es `StreamHandler`. Este manejador permite configurar el flujo para mostrar los mensajes directamente en la pantalla (salida estándar `sys.stderr` o `sys.stdout`), lo que resulta de gran utilidad para supervisar la ejecución y depurar el programa en tiempo real. Aunque es conceptualmente similar a la función integrada `print()`, `StreamHandler` ofrece un control mucho más preciso sobre el enrutamiento de los mensajes. Los manejadores se pueden asociar a los registradores mediante el método `addHandler()`.

### Ejemplo de registrador personalizado con StreamHandler

A continuación se muestra cómo configurar un registrador con un nivel de gravedad permisivo (`DEBUG`) y asociarle un `StreamHandler` con un nivel más restrictivo (`INFO`). Esto asegura que solo se muestren en consola los mensajes de nivel `INFO` o superior, a pesar de que el registrador base procese todos los mensajes.

```python
import logging

# Configuración del registrador (logger) y StreamHandler

# Se crea un registrador personalizado
stream_logger = logging.getLogger('stream_logger')
stream_logger.setLevel(logging.DEBUG)  # Captura todos los mensajes desde el nivel DEBUG en adelante

# Se asegura de limpiar manejadores previos asociados
stream_logger.handlers = []

# Se crea un manejador de consola (StreamHandler)
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Muestra en consola solo mensajes de nivel INFO en adelante

# Se asocia el manejador al registrador personalizado
stream_logger.addHandler(stream_handler)

# Se emiten mensajes en diferentes niveles de gravedad
stream_logger.debug("Este es un mensaje de DEBUG para stream_logger.")
stream_logger.info("Este es un mensaje de INFO para stream_logger.")
stream_logger.warning("Este es un mensaje de WARNING para stream_logger.")
stream_logger.error("Este es un mensaje de ERROR para stream_logger.")
stream_logger.critical("Este es un mensaje de CRITICAL para stream_logger.")
```

**Salida resultante en pantalla:**

```text
Este es un mensaje de INFO para stream_logger.
Este es un mensaje de WARNING para stream_logger.
Este es un mensaje de ERROR para stream_logger.
Este es un mensaje de CRITICAL para stream_logger.
```

*(El mensaje de nivel `DEBUG` es descartado por el manejador porque su nivel está configurado en `INFO`)*.

### Diferentes tipos de manejadores de registro

Además de `StreamHandler`, el módulo `logging` incorpora diversos manejadores especializados en el submódulo `logging.handlers`:

*   **`FileHandler`**: Dirige los mensajes de registro a un archivo en el disco.
*   **`NullHandler`**: Manejador que no realiza ninguna acción (útil para que las bibliotecas no muestren salida por defecto).
*   **`WatchedFileHandler`**: Variante de `FileHandler` que supervisa si el archivo externo ha cambiado o se ha rotado.
*   **`BaseRotatingHandler`**: Clase base para manejadores que rotan archivos al alcanzar ciertos límites.
*   **`RotatingFileHandler`**: Rota los archivos de registro basándose en el tamaño máximo del archivo.
*   **`TimedRotatingFileHandler`**: Rota los archivos de registro en intervalos de tiempo programados (horas, días, semanas, etc.).
*   **`SocketHandler`**: Envía los registros a un socket de red TCP/IP.
*   **`DatagramHandler`**: Envía los registros a través de UDP.
*   **`SysLogHandler`**: Envía mensajes a un demonio syslog de Unix/Linux.
*   **`NTEventLogHandler`**: Envía mensajes al visor de eventos de Windows (Event Log).
*   **`SMTPHandler`**: Envía los registros por correo electrónico mediante el protocolo SMTP.
*   **`MemoryHandler`**: Almacena los registros en memoria intermedia (buffer) y los libera bajo ciertas condiciones.
*   **`HTTPHandler`**: Envía registros a un servidor web mediante peticiones HTTP (GET o POST).
*   **`QueueHandler`**: Envía registros a una cola (útil para logging multiproceso o asíncrono).
*   **`QueueListener`**: Escucha los mensajes de una cola de registro y los pasa a los manejadores correspondientes.

