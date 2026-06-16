::page{title="Laboratorio práctico: Construyendo una API con Flask: Creación de rutas, Manejo de errores y Solicitudes HTTP"}

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/IDSN-logo.png" width="200/">

##

**Tiempo estimado necesario:** 45 minutos

##

Bienvenido a la parte 2 del laboratorio de Flask. Trabajarás con rutas y solicitudes HTTP en este laboratorio. Practicarás creando una pequeña API RESTful. Finalmente, trabajarás con controladores de errores a nivel de aplicación para errores comunes como:
- 404 NO ENCONTRADO
- 500 ERROR INTERNO DEL SERVIDOR

Deberías conocer todos los conceptos que necesitas para este laboratorio de la serie anterior de videos. Siéntete libre de pausar el laboratorio y revisar el módulo si no estás seguro de cómo realizar una tarea o necesitas más información.

## Objetivos de Aprendizaje

Después de completar este laboratorio, podrás:

- Escribir rutas para procesar solicitudes al servidor Flask en URLs específicas
- Manejar parámetros y argumentos enviados a las URLs
- Escribir controladores de errores para errores del servidor y del usuario

---

::page{title="Acerca de Skills Network Cloud IDE"}

Skills Network Cloud IDE (basado en Theia y Docker) proporciona un entorno para laboratorios prácticos relacionados con cursos y proyectos. Theia es un IDE de código abierto (Entorno de Desarrollo Integrado) que se ejecuta en escritorio o en la nube. Para completar este laboratorio, utilizarás el Cloud IDE basado en Theia y MongoDB ejecutándose en un contenedor Docker.

## Aviso Importante sobre este entorno de laboratorio

Ten en cuenta que las sesiones no persisten en este entorno de laboratorio. Cada vez que te conectes a este laboratorio, se creará un nuevo entorno para ti. Cualquier dato guardado en sesiones anteriores se perderá. Planea completar estos laboratorios en una sola sesión para evitar perder tus datos.

::page{title="Configurar el Entorno del Laboratorio"}

Hay algunas preparaciones necesarias que debes hacer antes de comenzar el laboratorio.

## Abre una Terminal

Abre una ventana de terminal usando el menú en el editor: **Terminal** > **Nueva Terminal**.

En la terminal, si no estás en la carpeta `/home/project`, cámbiate a tu carpeta de proyecto ahora.

```bash
cd /home/project
```


## Crear el directorio del laboratorio

Deberías tener un directorio del laboratorio de la Parte 1 del laboratorio. Si no tienes el directorio, créalo ahora.

```bash
mkdir lab
```


Cámbiate al directorio `lab`:

```bash
cd lab
```


Creaste un archivo `server.py` en el directorio del laboratorio en la Parte 1 del laboratorio. Crea el archivo si no está presente y añade el siguiente fragmento de código inicial a él.

```
# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Return a plain text response
    return "hello world"
```


> **Nota:** Asegúrate de que todo el código utilice una indentación de 4 espacios para evitar `IndentationError`.

Recuerda que el código anterior crea un servidor Flask y agrega un endpoint de inicio "/" que devuelve la cadena **hello world**. Ahora agregarás más código a este archivo en este laboratorio.

Como recordatorio, utiliza el siguiente comando para ejecutar el servidor desde la terminal:

```bash
flask --app server --debug run
```


![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-CD0320EN-SkillsNetwork/images/m1-flask-run-app.png "Ejecutar servidor Flask en modo depuración")

> **Nota:** Si el puerto `5000` está en uso, intenta con un puerto diferente como `5001`. Si el servidor no se inicia, revisa `server.py` en busca de errores de sintaxis o importaciones faltantes.

Ahora debes usar el comando CURL con `localhost:5000/`. Ten en cuenta que el terminal está ejecutando el servidor. Puedes usar el botón `Dividir Terminal` para dividir el terminal y ejecutar el siguiente comando en la segunda pestaña.

```bash
curl -X GET -i -w '\n' localhost:5000
```


### Opcional

Si trabajar en la terminal se vuelve difícil porque el símbolo del sistema es largo, puedes acortar el símbolo usando el siguiente comando:

```bash
export PS1="[\[\033[01;32m\]\u\[\033[00m\]: \[\033[01;34m\]\W\[\033[00m\]]\$ "
```


---

::page{title="Paso 1: Establecer el código de estado de respuesta"}

En la última parte, viste que Flask envía automáticamente una respuesta exitosa `HTTP 200 OK` cuando devuelves un mensaje. Sin embargo, también puedes establecer el estado de retorno de forma explícita. Recuerda que hay dos formas de hacerlo, como se discutió en el video:
1. Enviar una tupla de vuelta con el mensaje
2. Usar el método **make_response()** para crear una respuesta personalizada y establecer el estado

### Tus Tareas

1. Envía un código HTTP personalizado de vuelta con una tupla.

	Reutilizarás el archivo `server.py` en el que trabajaste en la última parte. Crea un nuevo método llamado `no_content` con el decorador `@app.route` y la URL de `/no_content`. El método no tiene argumentos. Devuelve una tupla con el mensaje JSON `No content found`.

<details>
	<summary>Haz clic aquí para obtener una pista.</summary>

> Puedes usar el siguiente código base como inicio:



```python
<insert @app decorator>
def <insert method name>():
    """return 'No content found' with a status of 204

    Returns:
        string: No content found
	    status code: 204
    """
    return ({insert dictionary here}, {insert HTTP code here})
```


</details>

Puedes probar el endpoint con el siguiente comando CURL:

```bash
curl -X GET -i -w '\n' localhost:5000/no_content
```


Deberías ver una salida similar a la siguiente. Toma nota del estado de `204` y del Content-Type de `application/json`. Ten en cuenta que, aunque devolviste un mensaje JSON, no se envía de vuelta al cliente como `204`. Por defecto, no se devuelve nada.

```
HTTP/1.1 204 NO CONTENT
Server: Werkzeug/2.2.2 Python/3.7.16
Date: Wed, 28 Dec 2022 19:49:18 GMT
Content-Type: application/json
Connection: close
```


### ¿Por qué usar 204?
El estado 204 No Content se utiliza en las API REST cuando una solicitud tiene éxito pero no se necesita devolver ningún dato. Por ejemplo:
- Después de eliminar un recurso (por ejemplo, un usuario), el servidor confirma el éxito sin enviar los datos eliminados.
- Al confirmar una acción (por ejemplo, actualizar configuraciones) sin información adicional.
- Aquí estamos devolviendo un mensaje JSON. Pero como estamos informando al cliente a través del código de estado 204 que no se devolverá contenido, la mayoría de los clientes HTTP ignorarán el cuerpo. Si necesitas mostrar un mensaje, utiliza el código de estado 200.

2. Envía un código HTTP personalizado de vuelta con el método `make_response()`. El método `make_response()` en Flask se utiliza para crear manualmente un objeto de respuesta HTTP completo, dándote más control sobre la respuesta que simplemente devolver un valor o una tupla.

	Crea un segundo método llamado `index_explicit` con el decorador `@app.route` y una URL de `/exp`. El método no tiene argumentos. Utiliza el método `make_response()` para crear una nueva respuesta. Establece el estado en 200.

	Asegúrate de importar `make_response` del módulo `flask`:
	```python
	from flask import Flask, make_response
	```

<details>
	<summary>Haz clic aquí para una pista.</summary>

```python
<insert @app decorator>
def <insert method name here>:
    """return 'Hello World' message with a status code of 200

    Returns:
        string: Hello World
        status code: 200
    """
    resp = make_response({insert ditionary here})
    resp.status_code = {insert status code here}
    return resp
```


</details>

Puedes probar el endpoint con el siguiente comando CURL:

```bash
curl -X GET -i -w '\n' localhost:5000/exp
```


Deberías ver una salida similar a la que se muestra a continuación. Nota el estado de `200`, el Content-Type de `application/json`, y la salida JSON de `{"message": "Hello World"}`:

```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.7.16
Date: Wed, 28 Dec 2022 19:55:46 GMT
Content-Type: application/json
Content-Length: 31
Connection: close

{
  "message": "Hello World"
}
```


### Solución
Verifica que tu trabajo coincida con la siguiente solución.
<details>
	<summary>Haz clic aquí para ver la respuesta.</summary>

```python
from flask import Flask, make_response

# Create an instance of the Flask class, passing in the name of the current module
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route("/")
def index():
    # Function that handles requests to the root URL
    # Return a plain text response
    return "hello world"

# Define a route for the "/no_content" URL
@app.route("/no_content")
def no_content():
    """Return 'no content found' with a status of 204.

    Returns:
        tuple: A tuple containing a dictionary and a status code.
    """
    # Create a dictionary with a message and return it with a 204 No Content status code
    return ({"message": "No content found"}, 204)

# Define a route for the "/exp" URL
@app.route("/exp")
def index_explicit():
    """Return 'Hello World' message with a status code of 200.

    Returns:
        response: A response object containing the message and status code 200.
    """
    # Create a response object with the message "Hello World"
    resp = make_response({"message": "Hello World"})
    # Set the status code of the response to 200
    resp.status_code = 200
    # Return the response object
    return resp
```


</details>

---

::page{title="Paso 2: Procesar argumentos de entrada"}

Es común que los clientes envíen argumentos en la URL. Aprenderás a procesar argumentos en este laboratorio. El laboratorio proporciona una lista de personas con su id, nombre, apellido e información de dirección en un objeto. Normalmente, esta información se almacena en una base de datos, pero estás utilizando una lista codificada para tu caso de uso simple. Estos datos fueron generados con [Mockaroo](https://www.mockaroo.com/ "Mockaroo").

El cliente enviará solicitudes en la forma de `http://localhost:5000?q=first_name`. Crearás un método que aceptará un first_name como entrada y devolverá a una persona con ese nombre.

<details>
	<summary>Haz clic aquí para copiar los datos en el archivo.</summary>

> Copia la siguiente lista en el archivo `server.py`:

```python
from flask import Flask, make_response
app = Flask(__name__)

data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]
```


</details>

Confirmemos que los datos se han copiado al archivo. Copia el siguiente código en el archivo **server.py** para crear un punto final que devuelva los datos de la persona al cliente en formato JSON.

```python
@app.route("/data")
def get_data():
    try:
        # Check if 'data' exists and has a length greater than 0
        if data and len(data) > 0:
            # Return a JSON response with a message indicating the length of the data
            return {"message": f"Data of length {len(data)} found"}
        else:
            # If 'data' is empty, return a JSON response with a 500 Internal Server Error status code
            return {"message": "Data is empty"}, 500
    except NameError:
        # Handle the case where 'data' is not defined
        # Return a JSON response with a 404 Not Found status code
        return {"message": "Data not found"}, 404

```


El código anterior simplemente verifica si la variable `data` existe. Si no existe, se genera un `NameError` y se devuelve un `HTTP 404`. Si los datos existen y están vacíos, se devuelve un `HTTP 500`. Si los datos existen y no están vacíos, se devuelve un mensaje de éxito `HTTP 200`.

Ejecuta un comando CURL para confirmar que recibes el mensaje de éxito:

```bash
curl -X GET -i -w '\n' localhost:5000/data
```


Resultado esperado:

```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.7.16
Date: Wed, 28 Dec 2022 20:51:56 GMT
Content-Type: application/json
Content-Length: 42
Connection: close

{
  "message": "Data of length 5 found"
}
```


### Tus Tareas

Crea un método llamado `name_search` con el decorador `@app.route`. Este método debe ser llamado cuando un cliente solicite la URL `/name_search`. El método no aceptará ningún parámetro, sin embargo, buscará el argumento `q` en la URL de la solicitud entrante. Este argumento contiene el first_name que el cliente está buscando. El método devuelve:
   - Información de la persona con un estado de `HTTP 200` si el first_name se encuentra en los datos.
   - Mensaje de `Parámetro de entrada inválido` con un estado de `HTTP 400` si el argumento `q` falta en la solicitud.
   - Mensaje de `Parámetro de entrada inválido` con un estado de `HTTP 422` si el argumento `q` está presente pero es inválido (por ejemplo, vacío o numérico).
   - Mensaje de `Persona no encontrada` con un código de estado de `HTTP 404` si la persona no se encuentra en los datos.

### Sugerencia
Asegúrate de importar el módulo `request` de Flask. Lo usarás para obtener el primer nombre de la solicitud HTTP.

```
from flask import request
```


Puedes usar el siguiente código como tu punto de partida:
<details>
	<summary>Haz clic aquí para una pista.</summary>

```python
@app.route("/name_search")
def name_search():
    """Find a person in the database.

    Returns:
        json: Person if found, with status of 200
        400: If argument 'q' is missing from the request
        422: If argument 'q' is present but invalid (e.g., empty or numeric)
        404: If person is not found in the data
    """
    # Get the argument 'q' from the query parameters of the request
    query = request.args.get('q')

    # Check if the query parameter 'q' is missing
    if query is None:
        return {"message": "Query parameter 'q' is missing"}, 400

    # Check if the query parameter is present but invalid (e.g., empty or numeric)
    if query.strip() == "" or query.isdigit():
        return {"message": "Invalid input parameter"}, 422

    # Iterate through the 'data' list to look for the person whose first name matches the query
    for person in data:
        if query.lower() in person["first_name"].lower():
            # If a match is found, return the person as a JSON response with a 200 OK status code
            return person, 200

    # If no match is found, return a JSON response with a message indicating the person was not found and a 404 Not Found status code
    return {"message": "Person not found"}, 404

```


</details>

Puedes probar el endpoint con el siguiente comando CURL. Asegúrate de que el servidor esté corriendo en la terminal como en los pasos anteriores.

```bash
curl -X GET -i -w '\n' "localhost:5000/name_search?q=Abdel"
```


Deberías ver una salida similar a la que se muestra a continuación. Nota el estado de `200`, el Content-Type de `application/json`, y la salida JSON de la persona con el nombre **Abdel**:

```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.7.16
Date: Wed, 28 Dec 2022 21:14:31 GMT
Content-Type: application/json
Content-Length: 295
Connection: close

{
  "address": "2 Lake View Point",
  "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
  "city": "Shreveport",
  "country": "United States",
  "first_name": "Abdel",
  "graduation_year": 1995,
  "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
  "last_name": "Duke",
  "zip": "71105"
}
```


A continuación, prueba que el método devuelve `HTTP 422` si el argumento `q` es inválido:

```bash
curl -X GET -i -w '\n' "localhost:5000/name_search?q=123"
```


o

```bash
curl -X GET -i -w '\n' "localhost:5000/name_search?q="
```


> **Nota:** Usa `HTTP 400` (Solicitud Incorrecta) cuando falte el parámetro de consulta requerido. Usa `HTTP 422` (Entidad No Procesable) solo si el parámetro está presente pero tiene contenido inválido o inaceptable.

Deberías ver una salida similar a la que se muestra a continuación. Observa el estado de `422`, el Content-Type de `application/json`, y la salida JSON de `Parámetro de entrada inválido`:

```
HTTP/1.1 422 UNPROCESSABLE ENTITY
Server: Werkzeug/2.2.2 Python/3.7.16
Date: Wed, 28 Dec 2022 21:16:07 GMT
Content-Type: application/json
Content-Length: 43
Connection: close

{
  "message": "Invalid input parameter"
}
```


Finalmente, probemos el caso en el que el first_name no está presente en nuestra lista de personas:

```bash
curl -X GET -i -w '\n' "localhost:5000/name_search?q=qwerty"
```


Deberías ver una salida similar a la que se muestra a continuación. Nota el estado de `404`, el Content-Type de `application/json`, y la salida JSON de `Persona no encontrada`:

```
HTTP/1.1 404 NOT FOUND
Server: Werkzeug/2.2.2 Python/3.7.16
Date: Wed, 28 Dec 2022 21:17:28 GMT
Content-Type: application/json
Content-Length: 36
Connection: close

{
  "message": "Person not found"
}
```


### Solución
Verifica que tu trabajo coincida con la siguiente solución. También hay otras formas de implementar esta solución.

<details>
	<summary>Haz clic aquí para ver la respuesta.</summary>

```python
@app.route("/name_search")
def name_search():
    """Find a person in the database based on the provided query parameter.

    Returns:
        json: Person if found, with status of 200
        404: If not found
        400: If the argument 'q' is missing
        422: If the argument 'q' is present but invalid (e.g., empty or numeric)
    """
    # Get the 'q' query parameter from the request URL
    query = request.args.get("q")

    # Check if the query parameter 'q' is missing
    if query is None:
        return {"message": "Query parameter 'q' is missing"}, 400

    # Check if the query parameter is present but invalid (empty or numeric)
    if query.strip() == "" or query.isdigit():
        return {"message": "Invalid input parameter"}, 422

    # Iterate through the 'data' list to search for a matching person
    for person in data:
        # Check if the query string is present in the person's first name (case-insensitive)
        if query.lower() in person["first_name"].lower():
            # Return the matching person as a JSON response with a 200 OK status code
            return person, 200

 # If no matching person is found, return a JSON response with a message and a 404 Not Found
    return {"message": "Person not found"}, 404

```


</details>

---

::page{title="Paso 3: Agregar URLs dinámicas"}

Una parte importante de la programación del lado del servidor es crear APIs. Una API es un contrato entre un proveedor y un usuario. Es común crear APIs RESTful que pueden ser llamadas por el front end u otros clientes. En una API basada en REST, la información del recurso se envía como parte de la URL de la solicitud. Por ejemplo, con tu recurso o personas, el cliente puede enviar la siguiente solicitud:

```
GET http://localhost/person/unique_identifier
```


Esta solicitud pide una persona con un identificador único. Otro ejemplo es:

```
DELETE http://localhost/person/unique_identifier
```


En este caso, el cliente solicita eliminar a la persona con este identificador único.

## Tus Tareas

Se te pide implementar ambos puntos finales en este ejercicio. También implementarás un método `count` que devuelve el número total de personas en la lista `data`. Esto ayudará a confirmar que los dos métodos GET y DELETE funcionan, como se requiere.

### Tarea 1: Crear el punto final GET /count

1. Crea el punto final **/count**.

	Agrega el decorador `@app.route()` para la URL `/count`. Define la función count que simplemente devuelve el número de elementos en la lista `data`.

	<details>
		<summary>Haz clic aquí para una pista.</summary>

	> Usa el método **len()** para devolver el número de elementos en la lista **data**.

	```
	@app.route("/count")
	def count():
		try:
			# Intenta devolver una respuesta JSON con el conteo de elementos en 'data'
			# Reemplaza {insert code to find length of data} con len(data) para obtener la longitud de la colección 'data'
			return {"data count": len(data)}, 200
		except NameError:
			# Si 'data' no está definido y genera un NameError
			# Devuelve una respuesta JSON con un mensaje y un código de estado 500 Internal Server Error
			return {"message": "data not defined"}, 500

	```
	</details>

	Prueba el método **count** llamando al punto final.
	```bash
	curl -X GET -i -w '\n' "localhost:5000/count"
	```

	Deberías ver una salida con el número de elementos en la lista de datos.
	```
	HTTP/1.1 200 OK
	Server: Werkzeug/2.2.2 Python/3.7.16
	Date: Sat, 31 Dec 2022 22:41:35 GMT
	Content-Type: application/json
	Content-Length: 22
	Connection: close

	{
	  "data count": 5
	}
	```

### Tarea 2: Crear el punto final GET /person/id

1. Implementa el punto final **GET** para solicitar una persona por id.

	Crea un nuevo punto final para `http://localhost/person/unique_identifier`. El método debe llamarse `find_by_uuid`. Debe tomar un argumento de tipo UUID y devolver la persona en formato JSON si se encuentra. Si la persona no se encuentra, el método debe devolver un 404 con un mensaje de **persona no encontrada**. Finalmente, el cliente (curl) solo podrá llamar a este método pasando un id de tipo UUID válido.

	<details>
		<summary>Haz clic aquí para una pista.</summary>

	> - usa la sintaxis type:name para permitir únicamente que los llamadores pasen un UUID válido.
	> - comparar uuid con string devuelve False. Asegúrate de convertir UUID a str al comparar con el atributo id de la persona.

	```bash
	@app.route("/person/<uuid:id>")
	def find_by_uuid(id):
		# Itera a través de la lista 'data' para buscar una persona con un ID coincidente
		for person in data:
			# Verifica si el campo 'id' de la persona coincide con el parámetro 'id'
			if person["id"] == str(id):
				# Devuelve la persona como una respuesta JSON si se encuentra una coincidencia
				return person

		# Devuelve una respuesta JSON con un mensaje y un código de estado 404 Not Found si no se encuentra ninguna persona coincidente
		return {"message": "Person not found"}, 404
	```
	</details>

	Prueba la URL **/person/uuid** llamando al punto final.
	```bash
	curl -X GET -i localhost:5000/person/66c09925-589a-43b6-9a5d-d1601cf53287
	```

	Deberías ver una salida con la persona y un código HTTP de 200.
	```
	HTTP/1.1 200 OK
	Server: Werkzeug/2.2.2 Python/3.7.16
	Date: Sat, 31 Dec 2022 22:48:32 GMT
	Content-Type: application/json
	Content-Length: 294
	Connection: close

	{
	  "address": "637 Carey Pass",
	  "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
	  "city": "Gainesville",
	  "country": "United States",
	  "first_name": "Lilla",
	  "graduation_year": 1985,
	  "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
	  "last_name": "Aupol",
	  "zip": "32627"
	}
	```

	Si pasas un UUID no válido, el servidor debe devolver un mensaje 404.
	```bash
	curl -X GET -i localhost:5000/person/not-a-valid-uuid
	```

	Deberías ver un error en la salida con un código de 404. Flask devuelve automáticamente HTML, cambiarás el HTML en la siguiente parte del laboratorio para devolver JSON por defecto en todos los errores, incluido el 404.
	```
	HTTP/1.1 404 NOT FOUND
	Server: Werkzeug/2.2.2 Python/3.7.16
	Date: Sat, 31 Dec 2022 22:50:52 GMT
	Content-Type: text/html; charset=utf-8
	Content-Length: 207
	Connection: close

	<!doctype html>
	<html lang=en>
	<title>404 Not Found</title>
	<h1>Not Found</h1>
	<p>The requested URL was not found on the server. If you entered the URL manually, please check your spelling and try again.</p>
	```

	Finalmente, pasa un UUID válido que no exista en la lista de datos. El método debe devolver un 404 con un mensaje de **persona no encontrada**.

	```bash
	curl -X GET -i localhost:5000/person/11111111-589a-43b6-9a5d-d1601cf51111
	```
	Deberías ver una respuesta JSON con un código HTTP de 404 y un mensaje de **persona no encontrada**.
	```
	HTTP/1.1 404 NOT FOUND
	Server: Werkzeug/2.2.2 Python/3.7.16
	Date: Sat, 31 Dec 2022 22:52:24 GMT
	Content-Type: application/json
	Content-Length: 36
	Connection: close

	{
	  "message": "person not found"
	}
	```
### Tarea 3: Crear el punto final DELETE /person/id

1. Implementa el punto final **DELETE** para eliminar un recurso persona.

	Crea un nuevo punto final para DELETE `http://localhost/person/unique_identifier`. El método debe llamarse `delete_by_uuid`. Debe tomar un argumento de tipo UUID y eliminar a la persona de la lista **data** con ese id. Si la persona no se encuentra, el método debe devolver un 404 con un mensaje de **persona no encontrada**. Finalmente, el cliente (curl) debe llamar a este método pasando un id de tipo UUID válido.

	<details>
		<summary>Haz clic aquí para una pista.</summary>

	> - usa la sintaxis type:name para permitir únicamente que los llamadores pasen un UUID válido.
	> - comparar uuid con string devuelve False. Asegúrate de convertir UUID a str al comparar con el atributo id de la persona.
	> - pasa el tipo de método **DELETE** como el segundo argumento al decorador @app o usa el decorador @app.delete().

	```bash
	@app.route("/person/<uuid:id>", methods=['DELETE'])
	def delete_person(id):
		for person in data:
			if person["id"] == str(id):
				# Elimina a la persona de la lista de datos
				data.remove(person)
				# Devuelve una respuesta JSON con un mensaje y el código de estado HTTP 200 (OK)
				return {"message": "Person with ID deleted"}, 200
		# Si no se encuentra ninguna persona con el ID dado, devuelve una respuesta JSON con un mensaje y el código de estado HTTP 404 (Not Found)
		return {"message": "Person not found"}, 404
	```
	</details>

	Prueba la URL DELETE **/person/uuid** llamando al punto final.
	```bash
	curl -X DELETE -i localhost:5000/person/66c09925-589a-43b6-9a5d-d1601cf53287
	```

	Deberías ver una salida con el id de la persona eliminada y un código de estado de 200.
	```
	HTTP/1.1 200 OK
	Server: Werkzeug/2.2.2 Python/3.7.16
	Date: Sat, 31 Dec 2022 23:00:17 GMT
	Content-Type: application/json
	Content-Length: 56
	Connection: close

	{
	  "message": "Person with ID 66c09925-589a-43b6-9a5d-d1601cf53287 deleted"
	}
	```

	Ahora puedes usar el punto final **count** que agregaste anteriormente para probar si el número de personas se ha reducido en uno.

	```bash
	curl -X GET -i localhost:5000/count
	```

	Deberías ver el conteo devuelto reducido en uno.

	```
	HTTP/1.1 200 OK
	Server: Werkzeug/2.2.2 Python/3.7.16
	Date: Sat, 31 Dec 2022 23:06:55 GMT
	Content-Type: application/json
	Content-Length: 22
	Connection: close

	{
	  "data count": 4
	}
	```

	Si pasas un UUID no válido, el servidor debe devolver un mensaje 404.
	```bash
	curl -X DELETE -i localhost:5000/person/not-a-valid-uuid
	```

	Deberías ver un error en la salida con un código de 404. Flask devuelve automáticamente HTML, y cambiaremos el HTML en la siguiente parte del laboratorio para devolver JSON por defecto en todos los errores, incluido el 404.
	```
	HTTP/1.1 404 NOT FOUND
	Server: Werkzeug/2.2.2 Python/3.7.16
	Date: Sat, 31 Dec 2022 23:05:09 GMT
	Content-Type: text/html; charset=utf-8
	Content-Length: 207
	Connection: close

	<!doctype html>
	<html lang=en>
	<title>404 Not Found</title>
	<h1>Not Found</h1>
	<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
	```

	Finalmente, pasa un UUID válido que no exista en la lista de datos. El método debe devolver un 404 con un mensaje de **persona no encontrada**.

	```bash
	curl -X DELETE -i localhost:5000/person/11111111-589a-43b6-9a5d-d1601cf51111
	```
	Deberías ver una respuesta JSON con un código HTTP de 404 y un mensaje de **persona no encontrada**.
	```
	HTTP/1.1 404 NOT FOUND
	Server: Werkzeug/2.2.2 Python/3.7.16
	Date: Sat, 31 Dec 2022 23:05:43 GMT
	Content-Type: application/json
	Content-Length: 36
	Connection: close

	{
	  "message": "person not found"
	}
	```

	### Solución
	Verifica que tu trabajo coincida con la siguiente solución.
	<details>
		<summary>Haz clic aquí para la respuesta.</summary>

	```python
	@app.route("/count")
	def count():
		try:
			# Intenta devolver el conteo de elementos en 'data' como una respuesta JSON
			return {"data count": len(data)}, 200
		except NameError:
			# Maneja el caso en que 'data' no está definido
			# Devuelve una respuesta JSON con un mensaje y un código de estado 500 Internal Server Error
			return {"message": "data not defined"}, 500

	@app.route("/person/<uuid:id>")
	def find_by_uuid(id):
		# Itera a través de la lista 'data' para buscar una persona con un ID coincidente
		for person in data:
			# Verifica si el campo 'id' de la persona coincide con el parámetro 'id'
			if person["id"] == str(id):
				# Devuelve la persona coincidente como una respuesta JSON con un código de estado 200 OK
				return person
		# Si no se encuentra ninguna persona coincidente, devuelve una respuesta JSON con un mensaje y un código de estado 404 Not Found
		return {"message": "person not found"}, 404

	@app.route("/person/<uuid:id>", methods=['DELETE'])
	def delete_by_uuid(id):
		# Itera a través de la lista 'data' para buscar una persona con un ID coincidente
		for person in data:
			# Verifica si el campo 'id' de la persona coincide con el parámetro 'id'
			if person["id"] == str(id):
				# Elimina a la persona de la lista 'data'
				data.remove(person)
				# Devuelve una respuesta JSON con un mensaje confirmando la eliminación y un código de estado 200 OK
				return {"message": f"Person with ID {id} deleted"}, 200
		# Si no se encuentra ninguna persona coincidente, devuelve una respuesta JSON con un mensaje y un código de estado 404 Not Found
		return {"message": "person not found"}, 404
	```
	</details>

---

::page{title="Paso 4: Analizar JSON del cuerpo de la solicitud"}

Vamos a crear otra API RESTful. El cliente puede enviar una solicitud `POST` a `http://localhost:5000/person` con el JSON de detalles de la persona como cuerpo. El servidor debe analizar la solicitud para el cuerpo y luego crear una nueva persona con ese detalle. En tu caso, para crear la persona, simplemente añade a la lista `data`.

### Tus Tareas

Crea un método llamado `add_by_uuid` con el decorador `@app.route`. Este método debe ser llamado cuando un cliente realice una solicitud con el método `POST` para la URL `/person`. El método no aceptará ningún parámetro, pero obtendrá los detalles de la persona del cuerpo JSON de la solicitud POST. El método devolverá:
- El `id` de la persona con un código de estado HTTP 200 si la persona se agrega correctamente a la lista `data`.
- Un mensaje `"Parámetro de entrada inválido"` con un código de estado HTTP 422 si el cuerpo JSON está ausente o vacío.

### Sugerencia
Asegúrate de importar el módulo `request` de Flask. Lo usarás para obtener el nombre de pila de la solicitud HTTP.

```python
from flask import request
```


Puedes usar el siguiente código como tu punto de partida. En el código de producción, deberías incluir alguna lógica para validar el JSON que llega. No querrías almacenar datos aleatorios que provienen de un cliente. Puedes omitir esta validación para tu caso de uso simple.
<details>
	<summary>Haz clic aquí para una pista.</summary>

```python
@app.route("/person", methods=['POST'])
def create_person():
    # Get the JSON data from the incoming request
    new_person = request.get_json()

    # Check if the JSON data is empty or None
    if not new_person:
        # Return a JSON response indicating that the request data is invalid
        # with a status code of 422 (Unprocessable Entity)
        return {"message": "Invalid input, no data provided"}, 422

    # Proceed with further processing of 'new_person', such as adding it to a database
    # or validating its contents before saving it

    # Assuming the processing is successful, return the person's id with status code 200
    return {"message": f"{new_person['id']}"}, 200
```


</details>

Puedes probar el endpoint con el siguiente comando CURL. Asegúrate de que el servidor esté en funcionamiento en la terminal como en los pasos anteriores.

```bash
curl -X POST -i -w '\n' \
  --url http://localhost:5000/person \
  --header 'Content-Type: application/json' \
  --data '{
        "id": "4e1e61b4-8a27-11ed-a1eb-0242ac120002",
        "first_name": "John",
        "last_name": "Horne",
        "graduation_year": 2001,
        "address": "1 hill drive",
        "city": "Atlanta",
        "zip": "30339",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff"
}'
```


Deberías ver una salida similar a la que se muestra a continuación. Nota el estado de `200`, el Content-Type de `application/json`, y la salida JSON de la persona con el primer nombre **Abdel**:

```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.7.16
Date: Sun, 01 Jan 2023 23:14:34 GMT
Content-Type: application/json
Content-Length: 56
Connection: close

{
  "message": "4e1e61b4-8a27-11ed-a1eb-0242ac120002"
}
```


También puedes probar el caso en el que envías un JSON vacío al endpoint utilizando el siguiente comando:

```bash
curl -X POST -i -w '\n' \
  --url http://localhost:5000/person \
  --header 'Content-Type: application/json' \
  --data '{}'
```


El servidor debe devolver un código 422 con un mensaje de `Invalid input parameter`.

```
HTTP/1.1 422 UNPROCESSABLE ENTITY
Server: Werkzeug/2.2.2 Python/3.7.16
Date: Sun, 01 Jan 2023 23:15:54 GMT
Content-Type: application/json
Content-Length: 43
Connection: close

{
  "message": "Invalid input parameter"
}
```


### Solución
Verifica que tu trabajo coincida con la siguiente solución. Hay más de una forma de implementar esta solución. Ten en cuenta que también debes comprobar si la lista `data` existe en la solución y devuelve un 500 si no es así.
<details>
	<summary>Haz clic aquí para ver la respuesta.</summary>

```python
@app.route("/person", methods=['POST'])
def add_by_uuid():
    new_person = request.json
    if not new_person:
        return {"message": "Invalid input parameter"}, 422
    # code to validate new_person ommited
    try:
        data.append(new_person)
    except NameError:
        return {"message": "data not defined"}, 500

    return {"message": f"{new_person['id']}"}, 200
```


</details>

---

::page{title="Paso 5: Agregar controladores de errores"}

En esta última parte del laboratorio, agregarás controladores globales a nivel de aplicación para manejar errores como 404 (no encontrado) y 500 (error interno del servidor). Recuerda del video que Flask facilita el manejo de estos controladores de errores globales utilizando el decorador errorhandler().

Si ahora haces una solicitud inválida al servidor, Flask devolverá una página HTML con el error 404. Algo como esto:

Comando:

```bash
curl -X POST -i -w '\n' http://localhost:5000/notvalid
```


Lo siento, no hay texto para traducir.

```
HTTP/1.1 404 NOT FOUND
Server: Werkzeug/2.2.2 Python/3.7.16
Date: Sun, 01 Jan 2023 23:21:54 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 207
Connection: close

<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually, please check your spelling and try again.</p>
```


Esto es genial, pero quieres devolver una respuesta JSON para todas las solicitudes no válidas.

### Tus Tareas

Crea un método llamado `api_not_found` con el decorador `@app.errorhandler`. Este método devolverá un mensaje de `API no encontrada` con un código de estado HTTP de `404` cada vez que el cliente solicite una URL que no conduzca a ningún endpoint definido por el servidor.

### Sugerencia
Utiliza el decorador `@app.errorhandler` y pasa el código HTTP de `404`.

Puedes usar el siguiente código como punto de partida:
<details>
	<summary>Haz clic aquí para una sugerencia.</summary>

```python
{insert errorhandler decorator here}({insert error code here})
def {insert method name here}(error):
    return {"message": "{insert error message here}"}, {insert error code here}
```


</details>

Puedes probar el endpoint con el siguiente comando CURL. Asegúrate de que el servidor esté en funcionamiento en la terminal, como en los pasos anteriores.

```bash
curl -X POST -i -w '\n' http://localhost:5000/notvalid
```


Deberías ver una salida similar a la que se muestra a continuación. Nota el estado de `404`, el Content-Type de `application/json` y el mensaje de salida en JSON de **API no encontrada**:

```
HTTP/1.1 404 NOT FOUND
Server: Werkzeug/2.2.2 Python/3.7.16
Date: Sun, 01 Jan 2023 23:25:35 GMT
Content-Type: application/json
Content-Length: 33
Connection: close

{
  "message": "API not found"
}
```


Ten en cuenta que el servidor ya no devuelve HTML sino JSON como se requiere.

### Solución
Verifica que tu trabajo coincida con la solución a continuación. Hay más de una forma de implementar esta solución.
<details>
	<summary>Haz clic aquí para ver la respuesta.</summary>

```python
@app.errorhandler(404)
def api_not_found(error):
    # This function is a custom error handler for 404 Not Found errors
    # It is triggered whenever a 404 error occurs within the Flask application
    return {"message": "API not found"}, 404
```


</details>

De manera similar, también puedes agregar un controlador de errores global para `500 (error interno del servidor)`.

Puedes registrar un controlador de errores global en Flask para cualquier excepción no manejada utilizando:

```bash
@app.errorhandler(Exception)
def handle_exception(e):
    return {"message": str(e)}, 500
```


Esto le indica a Flask que capture cualquier excepción no manejada que se genere en cualquier parte de su aplicación y la dirija a este controlador, devolviendo una respuesta de 500 Internal Server Error con el mensaje de error.

Puede provocar deliberadamente una excepción para probar el controlador global. Agregue la siguiente ruta antes de sus controladores de errores:

```bash
@app.route("/test500")
def test500():
    raise Exception("Forced exception for testing")

```


Luego ejecuta este comando curl en tu terminal:

```bash
curl http://localhost:5000/test500

```


Deberías ver una respuesta como:

```bash
{
  "message": "Forced exception for testing"
}

```


## Autor(es)
CF

## <h3 align="center"> &#169; IBM Corporation 2023. Todos los derechos reservados. <h3/>