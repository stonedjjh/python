# Requests

**Requests** es una biblioteca de Python elegante y sencilla para realizar peticiones HTTP. Está diseñada para ser amigable con el desarrollador, facilitando el envío de solicitudes HTTP/1.1 y la integración con servicios web sin necesidad de gestionar manualmente las cadenas de consulta de las URL o codificar los datos de tipo POST.

## Principales características de Requests

1. **Simplicidad:** Permite realizar peticiones HTTP con una cantidad mínima de líneas de código en comparación con la biblioteca estándar `urllib`.
2. **Decodificación automática:** Los datos de respuesta se decodifican automáticamente, lo que facilita la lectura de texto, JSON y contenido binario.
3. **Gestión de Sesiones (Sessions):** Mantiene la persistencia de cookies y configuraciones a través de múltiples peticiones al mismo host.
4. **Manejo de errores:** Proporciona mecanismos claros para detectar errores de conexión, tiempos de espera superados (timeouts) y códigos de estado HTTP incorrectos.

## Instalación de Requests

Para realizar la instalación de la biblioteca Requests, se debe ejecutar el siguiente comando en la consola del sistema:

```bash
pip install requests
```

## Concepto de Comunicación en Red y HTTP

Hasta este punto, se ha analizado cómo serializar datos para almacenarlos en disco (por ejemplo, con JSON o YAML). No obstante, este método requiere que los procesos compartan el mismo sistema de archivos. Para enviar mensajes a otros ordenadores a través de una red, se emplea el protocolo **HTTP** (HyperText Protocol).

La biblioteca **Requests** abstrae la complejidad de la conexión de red, la construcción de cabeceras y la decodificación de las respuestas, permitiendo realizar peticiones mediante métodos sencillos de Python.

---

## Ejemplos de uso de Requests

A continuación se presentan ejemplos que ilustran cómo utilizar la biblioteca para interactuar con servicios web.

### 1. Petición GET básica y lectura de texto

Una petición GET permite recuperar un recurso del servidor web a través de su URL (Uniform Resource Locator). El resultado obtenido es un objeto de tipo `requests.Response`.

```python
import requests

# Se realiza una petición HTTP GET a la página principal de Google
respuesta = requests.get("https://www.google.com")

# Se verifica si la petición fue exitosa (código de estado 200)
if respuesta.status_code == 200:
    # Se extraen y muestran únicamente los primeros 300 caracteres del texto HTML de la respuesta
    print("Primeros 300 caracteres de la respuesta:")
    print(respuesta.text[:300])
else:
    print(f"Error al realizar la petición. Código de estado: {respuesta.status_code}")
```

### 2. Envío de parámetros en la URL (Query Parameters)

Es posible pasar parámetros en la URL utilizando el argumento `params`. La biblioteca se encarga de codificar correctamente los caracteres especiales.

```python
import requests

# Se definen los parámetros de consulta en un diccionario
parametros = {
    "userId": 1,
    "id": 2
}

# Se realiza la petición GET incluyendo los parámetros
respuesta = requests.get("https://jsonplaceholder.typicode.com/posts", params=parametros)

# Se muestra la URL resultante con los parámetros codificados
print("URL final:", respuesta.url)

# Se procesa la respuesta como una estructura de Python si contiene JSON
datos = respuesta.json()
print("Datos recibidos:", datos)
```

### 3. Petición POST con datos (Form Data y JSON)

Una petición POST se emplea para enviar información al servidor (por ejemplo, para crear un nuevo recurso).

```python
import requests

# Datos que se enviarán como formulario web
datos_formulario = {
    "title": "Nuevo Artículo",
    "body": "Contenido del nuevo artículo.",
    "userId": 1
}

# Se realiza la petición POST con datos de tipo formulario
respuesta_formulario = requests.post("https://jsonplaceholder.typicode.com/posts", data=datos_formulario)
print("Respuesta POST (formulario) - Código:", respuesta_formulario.status_code)
print("Respuesta POST (formulario) - JSON:", respuesta_formulario.json())

# Datos que se enviarán como JSON
datos_json = {
    "title": "Otro Artículo",
    "body": "Contenido en formato JSON.",
    "userId": 2
}

# Se realiza la petición POST enviando datos directamente como JSON
respuesta_json = requests.post("https://jsonplaceholder.typicode.com/posts", json=datos_json)
print("Respuesta POST (JSON) - Código:", respuesta_json.status_code)
```

### 4. Cabeceras personalizadas (Headers)

Para simular una petición desde un navegador web específico o enviar credenciales (como tokens de API), se pueden personalizar las cabeceras.

```python
import requests

# Se definen las cabeceras personalizadas
cabeceras = {
    "User-Agent": "MiAplicacionPython/1.0",
    "Authorization": "Bearer TOKEN_DE_PRUEBA"
}

# Se ejecuta la petición GET con las cabeceras configuradas
respuesta = requests.get("https://httpbin.org/headers", headers=cabeceras)
print(respuesta.text)
```

### 5. Control de Tiempos de Espera (Timeouts) y Excepciones

Es una buena práctica definir un tiempo de espera límite (`timeout`) para evitar que el programa se quede suspendido indefinidamente si el servidor no responde.

```python
import requests
from requests.exceptions import Timeout, ConnectionError, HTTPError

try:
    # Se establece un límite de 3 segundos para la conexión y la lectura
    respuesta = requests.get("https://httpbin.org/delay/5", timeout=3)
    
    # Se lanza una excepción si el código de estado indica un error HTTP (por ejemplo, 404 o 500)
    respuesta.raise_for_status()
    
    print("Petición exitosa.")
except Timeout:
    print("La petición ha superado el tiempo de espera establecido.")
except ConnectionError:
    print("Se produjo un error al intentar conectarse al servidor.")
except HTTPError as error_http:
    print(f"Error HTTP ocurrido: {error_http}")
```

### 6. Uso de Sesiones (Sessions)

La clase `Session` permite persistir ciertos parámetros a lo largo de varias peticiones (como cookies o cabeceras comunes) y reutiliza la misma conexión TCP, mejorando el rendimiento.

```python
import requests

# Se crea un objeto de sesión
sesion = requests.Session()

# Se configura una cabecera que se aplicará a todas las peticiones de esta sesión
sesion.headers.update({"X-Token-Sesion": "123456"})

# Primera petición utilizando la sesión
respuesta1 = sesion.get("https://httpbin.org/cookies/set/usuario/antigravity")
print("Cookies actuales en la sesión:", sesion.cookies.get_dict())

# Segunda petición (mantiene las cookies configuradas previamente)
respuesta2 = sesion.get("https://httpbin.org/cookies")
print("Respuesta del servidor sobre las cookies:", respuesta2.text)
```

### 7. Acceso a datos crudos (Raw) y descompresión automática

La biblioteca Requests realiza de manera interna tareas complejas como la descompresión automática de datos codificados (por ejemplo, con `gzip`). Es posible comprobar las cabeceras involucradas y acceder a los bytes crudos (sin descomprimir) activando el parámetro `stream=True`.

```python
import requests

# Se realiza la petición activando la transmisión de flujo de datos (stream=True)
respuesta = requests.get("https://www.google.com", stream=True)

# Se leen los primeros 100 bytes del contenido binario crudo (comprimido)
bytes_crudos = respuesta.raw.read(100)
print("Primeros 100 bytes crudos (comprimidos):")
print(bytes_crudos)

# Se verifica que Requests indicó al servidor la capacidad de aceptar compresión (Accept-Encoding)
print("\nCabecera enviada en la petición (Accept-Encoding):", respuesta.request.headers.get("Accept-Encoding"))

# Se verifica si el servidor respondió indicando que el contenido fue comprimido (Content-Encoding)
print("Cabecera recibida en la respuesta (Content-Encoding):", respuesta.headers.get("Content-Encoding"))
```