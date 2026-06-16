# Operaciones CRUD utilizando características adicionales en Flask

## Descripción general

Crear, Leer, Actualizar y Eliminar (CRUD) son funciones básicas que cualquier aplicación con una base de datos debe realizar. Para implementar eficazmente las operaciones CRUD, necesitarás gestionar diferentes métodos HTTP, como las solicitudes GET y POST. Una solicitud GET se utiliza generalmente para recuperar o leer datos y a menudo se usa para mostrar un formulario. Una solicitud POST se utiliza comúnmente para enviar datos para crear o actualizar información. Un ejemplo de una solicitud POST es el envío de un formulario.

Esta lectura tiene como objetivo introducirte a características adicionales de Flask, centrándose en las funciones CRUD. También aprenderás cómo estas funciones están interrelacionadas y cómo utilizan los diferentes archivos HTML, rutas dinámicas y varios métodos HTTP.

## Objetivos

En esta lectura, usted:

- **Accederá a los datos del formulario** para capturar las entradas del usuario con `flask.request.form` en solicitudes `POST`
- Controlará la navegación del usuario: utilizando la función `redirect` de Flask
- **Generará URLs dinámicamente** usando `url_for` para crear URLs adaptables en su aplicación Flask
- **Gestionará diferentes tipos de solicitudes HTTP** para diseñar rutas flexibles que respondan a varios tipos de solicitudes HTTP
- **Implementará operaciones CRUD** para la gestión de datos en una aplicación Flask

Nota: Cada sección incluye ejemplos de código relevantes y explicaciones para mejorar su comprensión de las características cruciales de Flask.

## Accediendo a los Datos del Formulario con flask.request.form

Puedes usar flask.request.form para acceder a los datos del formulario que un usuario ha enviado a través de una solicitud POST. Por ejemplo, esta función se puede utilizar si tienes un formulario de inicio de sesión con campos de nombre de usuario y contraseña.

En tu archivo HTML, podrías tener un formulario como este:

```PYTHON
<form method="POST" action="/login">
    <input type="text" name="username">
    <input type="password" name="password">
    <input type="submit" value="Submit">
</form>
```

El código Python para acceder al nombre de usuario y la contraseña será el siguiente:

```PYTHON
from flask import request
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # process login here
```

## Redirigiendo a una URL con flask.redirect

Flask proporciona una función llamada flask.redirect para guiar a los usuarios a diferentes páginas web (o endpoints). La función flask.redirect puede ser útil en varios escenarios. Por ejemplo, puedes usar la función flask.redirect para redirigir a un usuario a una **página de inicio de sesión** cuando intenta acceder a una **página de administrador** restringida.

Código en Python:

```PYTHON
from flask import redirect
@app.route('/admin')
def admin():
    return redirect('/login')
```

## Generando URLs Dinámicas con flask.url_for

La función `flask.url`_for genera dinámicamente URLs para un endpoint dado. La generación dinámica de URLs puede ser particularmente útil cuando se altera la URL de una ruta. La función `flask.url`_for actualiza automáticamente la URL en tus plantillas o código, minimizando el trabajo manual. Por ejemplo, considera el escenario donde un usuario intenta acceder a la página de **admin** y debe ser redirigido a la página de **login**. En este escenario, `url_for('login')` recuperará la URL para la página de **login** de las rutas existentes.

Código en Python:

```PYTHON
from flask import url_for
@app.route('/admin')
def admin():
    return redirect(url_for('login'))
@app.route('/login')
def login():
    return "<Login Page>"
```

## Manejo de diferentes tipos de solicitudes HTTP

Flask te permite definir rutas para gestionar diferentes tipos de solicitudes HTTP. Puedes definir la ruta con ambos métodos de acceso, GET y POST, y en la descripción de la función, definir los casos de uso para ambos métodos.

Código en Python:

```PYTHON
@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        # process POST request
    if request.method == 'GET':
        # process GET request
```

En el archivo HTML, agregarás un formulario que permite tanto solicitudes `GET` como `POST`:

```PYTHON
<!-- For POST -->
<form method="POST" action="/data">
    <!-- Your input fields here -->
    <input type="submit" value="Submit">
</form>
<!-- For GET -->
<a href="/data">Fetch data</a>
```

En el último ejemplo, la ruta `/data` acepta tanto solicitudes `GET` como `POST`. El tipo de la solicitud se puede verificar usando `flask.request.method`.

## Operaciones CRUD

Las operaciones CRUD representan las cuatro funciones básicas que necesitas para interactuar con cualquier almacenamiento persistente, como una base de datos. En el desarrollo web, las operaciones CRUD a menudo corresponden a métodos HTTP.

### Crear operación

Crear datos a menudo implica presentar un formulario al usuario para recopilar la información que deseas almacenar en la base de datos como un nuevo registro. En Flask, estos datos se acceden utilizando `flask.request.form`.

Formulario HTML para crear datos:

```PYTHON
<form method="POST" action="/create">
    <input type="text" name="name">
    <input type="submit" value="Create">
</form>

# Este es un código de ejemplo en Python

def saludo(nombre):
    print(f"Hola, {nombre}!")
saludo("Mundo")


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Access form data
        name = request.form['name']
        # Create a new record with the name
        record = create_new_record(name)  # Assuming you have this function defined
        # Redirect user to the new record
        return redirect(url_for('read', id=record.id))
    # Render the form for GET request
    return render_template('create.html')
```

### Operación de lectura

Leer datos implica acceder a los datos y presentarlos al usuario. Para acceder a entradas específicas, la solicitud necesita ir con IDs específicos. Por lo tanto, necesitarás pasar el ID como un argumento a la función. El siguiente ejemplo muestra que el ID se puede acceder desde la ruta.

Código Python:

```PYTHON
@app.route('/read/<int:id>', methods=['GET'])
def read(id):
    # Get the record by id
    record = get_record(id)  # Assuming you have this function defined
    # Render a template with the record
    return render_template('read.html', record=record)
```

### Operación de actualización

Actualizar datos requiere el proceso de acceder a entradas específicas, como la operación de **Lectura**, e implica proporcionar nuevos datos al parámetro correspondiente, como la operación de **Creación**. Por lo tanto, la ruta debe acceder al ID y contener ambos métodos de acceso.

Ejemplo de formulario HTML para actualizar datos:

```PYTHON
<form method="POST" action="/update/{{record.id}}">
    <input type="text" name="name" value="{{record.name}}">
    <input type="submit" value="Update">
</form>

# This is a sample Python code

def greet(name):
    return f"Hello, {name}!"
print(greet("World"))


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        # Access form data
        name = request.form['name']
        # Update the record with the new name
        update_record(id, name)  # Assuming you have this function defined
        # Redirect user to the updated record
        return redirect(url_for('read', id=id))

    # Render the form for GET request with current data
    record = get_record(id)  # Assuming you have this function defined
    return render_template('update.html', record=record)
```

### Operación de eliminación

Eliminar datos implica quitar un registro basado en su ID. La operación de eliminación generalmente requerirá que se pase el ID, como se informa en la página HTML, en forma de argumento a la función.

Ejemplo de formulario HTML para eliminar datos:

```PYTHON
<form method="POST" action="/delete/{{record.id}}">
    <input type="submit" value="Delete">
</form>


# Este es un comentario en Python

def suma(a, b):
    return a + b
resultado = suma(5, 3)
print(resultado)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    # Delete the record
    delete_record(id)  # Assuming you have this function defined
    # Redirect user to the homepage
    return redirect(url_for('home'))
```
