# Flask

[Sitio web](https://flask.palletsprojects.com/es/stable/)

Creando en el 2004 por Armin Ronacher

## Características

- Es un micro framework, lo que significa que es ligero y fácil de usar.

- Desplegado en un servidor web

- Tiene un depurador.

- Usa el logging estandard de Python.

- Tiene integración con unit testing.

## Características Adicionales

- Admite activos estáticos como archivos css, javascript y html.

- Permite desarrollar páginas dinámicas usando el marco de plantillas Jinja2.

- Soporta enrutamiento Dinamico de URLS

- Soporta manejadores de errores globales

- Es compatible con el manejo de sesiones.

## Extensiones populares

- Flask-SQLAlchemy: para la integración con bases de datos SQL.

- Flask-Mail: para enviar correos electrónicos desde la aplicación.

- Flask-Admin: permite añadir fácilmente interfaces de administación a las aplicaciones de Flask.

- Flask-Uploads

- Flask-CORS: gestiona el intercambio de recursos entre dominios diferentes, posibilitanto las solicitudes de JavaScript de origen cruzado.

- Flask-Migrate: añade migraciones de bases de datos SQLAlchemy ORM.

- Flask-User: agrega la autenticación, autorización y otras actividades de administración de usuarios.

- Flask-WTF

- Marshmallow: añade soporte a la serialización y deserialización de objetos

- Cherry: para tareas sencillas en segundo plano

## Dependencias Integradas

- Werkzeug: un conjunto de herramientas WSGI para construir aplicaciones web.

- Jinja: lenguaje de plantilla para renderizar las páginas web.

- MarkupSafe: Viene con jinja y ayuda con la sanitización de los campos de entrada.

- ItsDangerous: Se usa para asignar valores de manera segura y proteger las cookie de sesión de Flask.

- Click: una biblioteca para crear interfaces de línea de comandos, utilizada por Flask para proporcionar comandos de administración.

## Como iniciar una aplicacion

1. Crea un entorno virtual para tu proyecto:

   ```bash
   python -m venv env
   ```

2. Activa el entorno virtual:
   - En Windows:

     ```bash
     .\env\Scripts\activate
     ```

   - En macOS/Linux:

     ```bash
     source env/bin/activate
     ```

3. Instala Flask:

   ```bash
   pip install flask
   ```

4. Crea un archivo `app.py` con el siguiente contenido:

   ```python
    from flask import Flask
    my_app = Flask("My first Application")

    @my_app.route("/")
    def home():
        return "Hello, Flask!"

    if __name__ == "__main__":
        my_app.run(debug=True)
   ```

## Funciones dentro de Flask

- `jsonify()`: Serializa los argumentos dados como JSON, y devuelve un objeto Response con el mimetype application/json. Un dict o una lista devuelta desde una vista se convertirá en una respuesta JSON automáticamente sin necesidad de llamar a esto.

Se pueden dar argumentos posicionales o de palabra clave, pero no ambos. Si no se dan argumentos, se serializa None.

Parámetros:
`args` (t.Any) – Un único valor a serializar, o múltiples valores a tratar como una lista a serializar.

`kwargs` (t.Any) – Tratar como un dict para serializar.

**Ejemplos:**

```PYTHON
return jsonify({"message": "Hello World"}) # equivalente a jsonify(message="Hello World")
# {
#   "message": "Hello World"
# }

return jsonify("message", "Hello World")
# [
#   "message",
#   "Hello World"
# ]
```

- `make_response()`: Se usa para crear un objeto de respuesta

**Ejemplo:**

```PYTHON
from flask import Flask, make_response

@app.route("/exp")
def index_explicit():
    res = make_response({"Message": "respuesta explicita"})
    res.status = 200
    return res
```

- `request`: Se utiliza para hacer peticiones http.

## Decoradores

- `@app.route(<path>)`: Decora una función de la vista para registrarla con la regla de URL y las opciones dadas.

   **sintaxis:** route(rule, **options)

   **ejemplos:**

   ```PYTHON
   #Ejemplo de un decorador sin opciones
   @app.route("/") # sino se especifica el método por defecto sera GET
   #Ejemplo de un decorador pasando el método
   @app.route("/", methods=["GET"]) # Puede pasar una lista de método soportados methods=["GET", "POST"]
   ```

   **Componentes**

  - `Request Object`: El objeto de solicitud utilizado por defecto en Flask. Recuerda el endpoint coincidente y los argumentos de la vista.

    Algunos atributos de la clase request son:

    - **server**: retorna la dirección del servidor en la forma de una tupla host port

    - **headers**: retorna la cabezera enviada con la petición.​

         La cabezera tambien contiene la siguiente data

      - **Cache-Control**: contiene información sobre cómo almacenr en caché en los navegadores.

      - **Accept**: informa al navegador quué tipò de contnido entiende el cliente.

      - **Accept-Encoding**: identifica el cliente, la aplicación, el sistema operativo o la versión.

      - **Host**: especifica el host y el número de puerto del servidor solicitado.

    - **URL**: retorna la URL que es el recurso pedido por la petición.

    - **access_route**: retorna la lista de todas las direcciones IP para peticiones.

    - **full_path**: que representa la ruta completa de la petición, incluyendo los query string.

    - **is_secure**: devuelve un booleano si el cliente esta realizando una solicitud utilizando el protocolo HTTPS o WSS.

    - **is_JSON**: devuelve un booleano si la solicitud contiene datos JSON.

    - **cookies**: devuelve un diccionario que contiene cualquier cookie enviada con la solicitud.

    - **method**: devuelve el método con el que se invoco a la ruta.

    Algunos métodos de la clase request son:

    - **get_data**: para acceder a los datos de la petición POST como bytes.

    - **get_JSON**: para obtener los datos parseados como JSON.

    - **args**: retorna los parámetros de la consulta como un diccionario.

    - **JSON**: analizará los datos en un diccionario.  

    - **files**: proporciona los archivos subidos por el usuario como un diccionario inmutable.

    - **form**: retorna un diccionario inmutable con los valores publicados en el envío de formulario.

    - **values**: retorna un diccionario que comina los datos de `args` con los datos del `form`.

    **Ejemplo:**

    Dada la siguiente URL: <http://localhost:5000?course=capstone&rating=10>

    ```PYTHON
    course = request.args["course"]
    rating = request.args.get("rating")
    ```
  
  - `Response Object`

    Algunos atributos de la clase response son:

    - **status_code**: retorna el código de estado de la solicitud.

    - **headers**: dara más informacion sobre la respuestas.

    - **content_type**: muestra el tipo de contenido del medio del recurso solicitado.

    - **content_length**: retorna la longitud del contenido, es el tamaño del cuerpo del mensaje de respuesta.

    - **content_encoding**: muestra la codificación del contenido.

    - **mimetype**: establece tl tipo de medio de la respuesta.

    - **expires**: contiene la fecha u hora tras la cual la repuesta se considera caducada.

    Algunos metodos de la clase response son:

    - **set_cookies**: establece una cookie del navegador en el cliente.

    - **delete_cookies**: elimina una cookie en el cliente.

## LLamar a APIs externas

```PYTHON
from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def get_author():
    res = requests.get("https://openlibrary.org/search/authors.JSON?q=Michael Crichton")
    if res.status_code == 200:
      return {"message" : res.JSON()}
    elif res.status_code == 404:
      return {"message" : "Something went wrong!"}, 404
    else:
      return {"message" : "Server error"}, 500
```

## Enrutamiento Dinámico

```PYTHON
from flask import Flask, escape
import requests

app = Flask(__name__)

@app.route("/book/<isbn>") # se puede definir el tipo de parmetro esperado @app.route("/book/<int:isbn>") 
def get_author(isbn):
    res = requests.get("https://openlibrary.org/isbn/{escape(isbn)}.JSON")
    if res.status_code == 200:
      return {"message" : res.JSON()}
    elif res.status_code == 404:
      return {"message" : "Something went wrong!"}, 404   
```

## Manejo de errores de solicitudes

### HTTP return status

- Cada respuesta consta de un código de estatus de 3 dígitos.

- Las respuestas validan van en el rango del 100 hasta el 599.

|Código|Descripción|
|:---|:----------|
|1xx|Informativos: indican que la solicitud se ha recibido|
|2xx|Exitosa: indican que la solicitud se ha recibido y se ha realizado correctamente|
|3xx|Redirección: indican que la solicitud se ha recibido y se ha redirigido|
|4xx|Error en la solicitud: indican un error en la solicitud|
|5xx|Error del servidor: indican un error en el lado del servidor|

|Código|Descripción|
|:---|:----------|
|200|La petición se ha realizado exitosamente|
|201|El recurso se creo con exito|
|202|La petición ha sido aceptada y esta en proceso|
|204|Se completo la petición con exito pero no devuelve ningún contenido|
|205|Error del servidor: indican un error en el lado del servidor|
|400|Indica una solicitud no válida|
|401|Indica que las credenciales faltan o no son válidas|
|403|La autorización no es suficiente|
|404|Recurso no encontrado|
|405|Operación no soportada|
|400|Error en el servidor|
