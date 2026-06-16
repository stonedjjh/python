# Flask

[Sitio web](https://flask.palletsprojects.com/es/stable/)

Creando en el 2004 por Armin Ronacher

## Características

- Es un micro framework, lo que significa que es ligero y fácil de usar.

- Desplegado en un servidor web

- Tiene un depurador.

- Usa el logging estandard de Python.

- Tiene integración con unit testing.

### ## Características Adicionales

- Admite activos estáticos como archivos css, javascript y html.

- Permite desarrollar páginas dinámicas usando el marco de plantillas Jinja2.

- Soporta enrutamiento Dinamico de URLS

- Soporta manejadores de errores globales

- Es compatible con el manejo de sesiones.

## Extensiones populares.

- Flask-SQLAlchemy: para la integración con bases de datos SQL.

- Flask-Mail: para enviar correos electrónicos desde la aplicación.

- Flask-Admin: permite añadir fácilmente interfaces de administación a kas aokucacuibes de Flask.

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
