::page{title="Laboratorio práctico: Diseño de aplicación CRUD utilizando características adicionales en Flask"}

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0INQEN/IDSN-logo.png" width="200" alt="logo de cognitiveclass.ai"  />

##

Tiempo estimado: **60** minutos 

## Descripción general
CRUD, que significa Crear, Leer, Actualizar, Eliminar, son funcionalidades básicas que cualquier aplicación basada en una base de datos debe poseer. El desarrollo de estas características requiere conocimientos adicionales sobre el manejo de rutas y solicitudes. También se requieren múltiples interfaces HTML de punto final para acomodar diferentes solicitudes. El propósito de este laboratorio, por lo tanto, es brindarte una práctica adicional sobre el uso de Flask y desarrollar una aplicación web completamente funcional capaz de realizar operaciones CRUD.

Para este laboratorio, desarrollarás un sistema de registro de transacciones financieras. El sistema debe ser capaz de **Crear** una nueva entrada, **Leer** entradas existentes, **Actualizar** entradas existentes y **Eliminar** entradas existentes.

## Objetivos

Después de completar este laboratorio, podrás:

- Implementar la operación "Crear" para agregar una entrada de transacción
- Implementar la operación "Leer" para acceder a la lista de entradas de transacción
- Implementar la operación "Actualizar" para actualizar los detalles de una entrada de transacción dada
- Implementar la operación "Eliminar" para eliminar una entrada de transacción.

Una vez que completes el desarrollo de la aplicación, funcionará como se muestra en la animación.<br>
La aplicación tiene tres páginas web diferentes. La primera muestra todas las transacciones registradas. Esta página se llama Registros de Transacciones y muestra todas las entradas de transacciones creadas en el sistema. Esta página también ofrece la opción de Editar y Eliminar las entradas disponibles. La opción de agregar una entrada también está disponible en esta página. La segunda página es Agregar Transacción, que se utiliza cuando el usuario elige agregar la entrada en la página anterior. El usuario agrega los valores de Fecha y Monto para la nueva entrada. La tercera página es Editar Transacción, a la que el usuario navega al hacer clic en la opción de editar entrada. En esta página también se aceptan la fecha y el monto como entradas; sin embargo, estas entradas se reflejan contra el ID que se estaba editando.
![ezgif com-video-to-gif](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0INQEN/ezgif.com-video-to-gif%20%282%29.gif)
Nota: Esta plataforma no es persistente. Se recomienda que mantengas una copia de tu código en tus máquinas locales y guardes los cambios de vez en cuando. En caso de que vuelvas a visitar el laboratorio, necesitarás recrear los archivos en este entorno de laboratorio utilizando las copias guardadas de tus máquinas.

¡Comencemos!

::page{title="Clonar el Repositorio del Proyecto"}

Este laboratorio requiere múltiples archivos de interfaz HTML, que han sido precreados para ti. Necesitarás clonar la estructura de carpetas en la interfaz del IDE utilizando el siguiente comando en una terminal.

```
git clone https://github.com/ibm-developer-skills-network/obmnl-flask_assignment.git
```


Cuando el comando se ejecute con éxito, la pestaña del Proyecto debe tener la estructura de carpetas como se muestra en la imagen. La carpeta raíz, `obmnl-flask_assignment`, debe tener la carpeta `templates` y un archivo `app.py`. La carpeta `templates` contiene todos los archivos HTML requeridos: `edit.html`, `form.html` y `transactions.html`. A lo largo de este laboratorio, implementarás las funciones necesarias en `app.py`.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0INQEN/Screenshot%202023-07-20%20at%204.35.01%20AM.png"  style="margin-top:10px; margin-bottom:10px" alt="Pestaña del proyecto con estructura de carpetas"  />

::page{title="Configuración inicial"}

En el `app.py`, necesitas importar los módulos necesarios de Flask e instanciar la aplicación Flask.  
Para este laboratorio, deberás importar las siguientes funciones de la ***flask*** library.  
- Flask - para instanciar la aplicación  
- request - para procesar las solicitudes `GET` y `POST`  
- url_for - para acceder a la url de una función dada usando su decorador  
- redirect - para redirigir las solicitudes de acceso según sea necesario  
- render_template - para renderizar la página html  

Después de importar las funciones, instancia la aplicación en una variable `app`.  

<details><summary><i>Haz clic aquí para obtener una pista</i></summary>

```python
from flask import <functions>
```


</details>
<details><summary><i>Haz clic aquí para la solución</i></summary>

```python
# Import libraries
from flask import Flask, redirect, request, render_template, url_for

# Instantiate Flask functionality
app = Flask(__name__)
```


Ahora, el código se verá así:
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0INQEN/Screenshot%202023-07-20%20at%204.42.38%20AM.png" alt="Referencia de código correcto" />

</details>

A continuación, creemos una lista de transacciones de muestra para fines de prueba. Puedes asumir que las transacciones ya existen en la interfaz cuando se ejecute por primera vez. Ten en cuenta que este paso es completamente opcional y no afecta la funcionalidad que desarrollarás en este laboratorio. Agrega el fragmento de código como se muestra a continuación en `app.py`.

```
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]
```


<details><summary><i>Haz clic aquí para la solución</i></summary>

![Datos de muestra](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0INQEN/Screenshot%202023-07-20%20at%204.43.05%20AM.png)

</details>

El orden en el que desarrollarás las funciones es el siguiente:
	1. Leer
	2. Crear
	3. Actualizar
	4. Eliminar
La razón para implementar **Leer** antes que las otras funciones es poder redirigir a la página con todas las transacciones cada vez que se crea, actualiza o elimina una nueva transacción. Por lo tanto, la función para leer las transacciones existentes debe existir antes de que se implementen las otras.

::page{title="Operación de Lectura"}

Para implementar la operación de **Lectura**, necesitas implementar una ruta que muestre una lista de todas las transacciones. Esta ruta manejará solicitudes `GET`, que se utilizan para recuperar y mostrar datos en `app.py`.

Los pasos clave para implementar la operación de Lectura son los siguientes:

1. Crea una función llamada `get_transactions` que utilice `render_template` para devolver una plantilla HTML llamada `transactions.html`. Esta función debe pasar las transacciones a la plantilla para su visualización.

2. Utiliza el decorador `@app.route` de Flask para mapear esta función a la URL raíz (`/`). Esto significa que cuando un usuario visite la URL base de tu aplicación, Flask ejecutará la función `get_transactions` y devolverá su resultado.

<details><summary><i>Haz clic aquí para una pista</i></summary>
Esta función es una función básica de render_template como se implementó en los laboratorios anteriores.
</details>	
	
<details><summary><i>Haz clic aquí para la solución</i></summary>
  

```python
# Read operation: List all transactions
@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions)
```


Ahora, el código se verá así:
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0INQEN/Screenshot%202023-07-20%20at%204.43.13%20AM.png" alt="Código correcto resaltado en rojo" >

</details>

::page{title="Crear Operación"}

Para la operación **Crear**, implementarás una ruta que permita a los usuarios agregar nuevas transacciones. Esto implicará manejar tanto solicitudes HTTP `GET` como `POST` - `GET` para mostrar el formulario al usuario y `POST` para procesar los datos del formulario enviados por el usuario.

Aquí está la lista de pasos para implementar la operación Crear.

1. Crea una función llamada `add_transaction`.

2. Usa `add` como el decorador para esta función. Asegúrate de pasar tanto `GET` como `POST` como métodos posibles.

3. Si el método de la solicitud es `GET`, usa la función `render_template` para mostrar un formulario HTML utilizando una plantilla llamada `form.html`. Este formulario permitirá a los usuarios ingresar datos para una nueva transacción.

4. Si el método de la solicitud es `POST`, utiliza `request.form` para extraer los datos del formulario, crear una nueva transacción, agregarla a la lista de transacciones y luego usar `redirect` y `url_for` para enviar al usuario de vuelta a la lista de transacciones.

5. La nueva transacción se pasa a la función de lectura en el siguiente formato.

```python
transaction  = {
	          'id': len(transactions)+1
	          'date': request.form['date']
	          'amount': float(request.form['amount'])
	         }
```


Aquí, la función request.form analiza la información recibida de la entrada realizada en el formulario.

<details><summary><i>Haz clic aquí para obtener una pista</i></summary>
El contenido de la función add_transaction necesita las siguientes implementaciones.

Para el método `POST`, crea la nueva transacción como se muestra arriba, añádela a la lista existente de transacciones y redirige a la URL para la operación de **Lectura**.

Para el método `GET`, renderiza la página form.html que acepta la información de la interfaz.
</details>

<details><summary><i>Haz clic aquí para ver la solución</i></summary>

```python
# Create operation: Display add transaction form
# Route to handle the creation of a new transaction
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Create a new transaction object using form field values
        transaction = {
            'id': len(transactions) + 1,            # Generate a new ID based on the current length of the transactions list
            'date': request.form['date'],           # Get the 'date' field value from the form
            'amount': float(request.form['amount']) # Get the 'amount' field value from the form and convert it to a float
        }
        # Append the new transaction to the transactions list
        transactions.append(transaction)

        # Redirect to the transactions list page after adding the new transaction
        return redirect(url_for("get_transactions"))
    
    # If the request method is GET, render the form template to display the add transaction form
    return render_template("form.html")

```


Ahora, el código se verá así:
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0INQEN/Screenshot%202023-07-20%20at%204.43.38%20AM.png" alt="Código correcto" >

Nota: Las declaraciones fuera del caso `if` son, por defecto, el caso `else`. Las declaraciones en el caso `if` terminan con una declaración de retorno; por lo tanto, solo uno de los dos casos se ejecutará a la vez.

::page{title="Operación de Actualización"}

Para la operación de **Actualización**, necesitas implementar una ruta que permita a los usuarios actualizar transacciones existentes. Nuevamente, manejarás tanto las solicitudes HTTP `GET` como `POST` - `GET` para mostrar los datos actuales de la transacción en un formulario, y `POST` para procesar los datos actualizados enviados por el usuario.

Completa los siguientes pasos para implementar la operación de Actualización.

1. Crea una función llamada `edit_transaction` que maneje tanto las solicitudes `GET` como `POST`. Esta función debe aceptar un parámetro, `transaction_id`.

2. Decora la función con `@app.route` y utiliza la cadena de ruta `/edit/<int:transaction_id>`. La parte `<int:transaction_id>` en la URL es un marcador de posición para cualquier entero. Flask pasará este entero a tu función como el argumento `transaction_id`.

3. Si el método de solicitud es `GET`, encuentra la transacción con el ID que coincide con `transaction_id` y utiliza `render_template` para mostrar un formulario pre-poblado con los datos actuales de la transacción utilizando una plantilla llamada `edit.html`.

4. Si el método de solicitud es `POST`, utiliza request.form para obtener los datos actualizados, encuentra la transacción con el ID que coincide con `transaction_id` y modifica sus datos, luego redirige al usuario de vuelta a la lista de transacciones.

<details><summary><i>Haz clic aquí para ver la solución</i></summary>

```python
# Update operation: Display edit transaction form
# Route to handle the editing of an existing transaction
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Extract the updated values from the form fields
        date = request.form['date']           # Get the 'date' field value from the form
        amount = float(request.form['amount'])# Get the 'amount' field value from the form and convert it to a float

        # Find the transaction with the matching ID and update its values
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date       # Update the 'date' field of the transaction
                transaction['amount'] = amount   # Update the 'amount' field of the transaction
                break                            # Exit the loop once the transaction is found and updated

        # Redirect to the transactions list page after updating the transaction
        return redirect(url_for("get_transactions"))
    
    # If the request method is GET, find the transaction with the matching ID and render the edit form
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            # Render the edit form template and pass the transaction to be edited
            return render_template("edit.html", transaction=transaction)

    # If the transaction with the specified ID is not found, handle this case (optional)
    return {"message": "Transaction not found"}, 404

```


Ahora, el código se verá así:
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0INQEN/Screenshot%202023-07-20%20at%204.43.51%20AM.png" alt="Referencia de código correcto">

Nota: Puede haber múltiples formas de lograr el mismo resultado. Por favor, utiliza la solución dada arriba solo como referencia.
</details>

::page{title="Operación de Eliminación"}

Finalmente, necesitas implementar una ruta que permita a los usuarios eliminar transacciones existentes.

Completa los siguientes pasos para implementar la operación de eliminación.

1. Crea una función llamada `delete_transaction` que tome un parámetro, `transaction_id`.

2. Decora la función con `@app.route` y utiliza la cadena de ruta `/delete/<int:transaction_id>`. La parte `<int:transaction_id>` en la URL es un marcador de posición para cualquier entero. Flask pasará este entero a tu función como el argumento `transaction_id`.

3. En el cuerpo de la función, encuentra la transacción con el ID que coincida con `transaction_id` y elimínala de la lista de transacciones, luego `redirect` al usuario de vuelta a la lista de transacciones.
	
<details><summary><i>Haz clic aquí para ver la solución</i></summary>

```python
# Delete operation: Delete a transaction
# Route to handle the deletion of an existing transaction
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    # Find the transaction with the matching ID and remove it from the list
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)  # Remove the transaction from the transactions list
            break  # Exit the loop once the transaction is found and removed

    # Redirect to the transactions list page after deleting the transaction
    return redirect(url_for("get_transactions"))

```


Ahora, el código se verá así:
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0INQEN/Screenshot%202023-07-20%20at%204.44.06%20AM.png" alt="Referencia de código correcta">
</details>

::page{title="Pasos Finales y Ejecución de la Aplicación"}

Verifica si el script actual es el programa principal (es decir, no fue importado desde otro script) con la condición `if __name__ == "__main__":`.

Si la condición es verdadera, llama a `app.run(debug=True)` para iniciar el servidor de desarrollo de Flask con el modo de depuración habilitado. Esto te permitirá ver mensajes de error detallados en tu navegador si algo sale mal.

```python
# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)

```


Ahora, el código se verá así:
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0INQEN/Screenshot%202023-07-20%20at%204.44.12%20AM.png" alt="Referencia de código correcto">
</details>

El código ahora está completo. Ejecuta el archivo `app.py` desde una terminal usando el comando:

```bash
python3.11 app.py
```


Por defecto, Flask lanza la aplicación en LocalHost:5000. Como se muestra en la imagen,
1. Lanza la aplicación yendo a la Biblioteca de Skills Network, y seleccionando `Launch Application`.
2. Ingresa `5000` en el número de puerto y lanza la ventana de la aplicación. 

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0INQEN/app_deploy.png">

	

La aplicación final se ve así. 

![ezgif com-video-to-gif](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0INQEN/ezgif.com-video-to-gif.gif)

::page{title="Ayuda de Laboratorio"}

En caso de que enfrentes un error al seguir todos los pasos, el código final para `app.py` se comparte aquí como referencia. Ten en cuenta que esto debe usarse solo como último recurso para asegurarte de que obtienes el aprendizaje previsto a través de este laboratorio.

<details><summary><i>Código final para app.py</i></summary>

```python
# Import necessary libraries from Flask
from flask import Flask, redirect, request, render_template, url_for
# Instantiate Flask application
app = Flask(__name__)
# Sample data representing transactions
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]
# Read operation: Route to list all transactions
@app.route("/")
def get_transactions():
    # Render the transactions list template and pass the transactions data
    return render_template("transactions.html", transactions=transactions)
# Create operation: Route to display and process add transaction form
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == 'POST':
        # Extract form data to create a new transaction object
        transaction = {
            'id': len(transactions) + 1,          # Generate a new ID based on the current length of the transactions list
            'date': request.form['date'],         # Get the 'date' field value from the form
            'amount': float(request.form['amount']) # Get the 'amount' field value from the form and convert it to a float
        }
        # Append the new transaction to the transactions list
        transactions.append(transaction)
        # Redirect to the transactions list page after adding the new transaction
        return redirect(url_for("get_transactions"))
    # Render the form template to display the add transaction form if the request method is GET
    return render_template("form.html")
# Update operation: Route to display and process edit transaction form
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method == 'POST':
        # Extract the updated values from the form fields
        date = request.form['date']
        amount = float(request.form['amount'])
        # Find the transaction with the matching ID and update its values
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date       # Update the 'date' field of the transaction
                transaction['amount'] = amount   # Update the 'amount' field of the transaction
                break                            # Exit the loop once the transaction is found and updated
        # Redirect to the transactions list page after updating the transaction
        return redirect(url_for("get_transactions"))
    # Find the transaction with the matching ID and render the edit form if the request method is GET
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            # Render the edit form template and pass the transaction to be edited
            return render_template("edit.html", transaction=transaction)
    # If no transaction with the matching ID is found, return a 404 error
    return {"message": "Transaction not found"}, 404
# Delete operation: Route to delete a transaction
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    # Find the transaction with the matching ID and remove it from the list
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)  # Remove the transaction from the transactions list
            # Redirect to the transactions list page after deleting the transaction
            return redirect(url_for("get_transactions"))
    # If no transaction with the matching ID is found, return a 404 error
    return {"message": "Transaction not found"}, 404
# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```


</details>

::page{title="Probando la Interfaz"}

Una vez que tu aplicación esté lista, prueba las operaciones CRUD en la aplicación lanzada. Las tareas posibles para probar la aplicación podrían ser:

1. Haz clic en el botón "Agregar" para abrir el formulario y añadir una nueva transacción.
	
2. Haz clic en el botón "Editar" para cualquier transacción y actualiza la información (fecha y monto) de la transacción.

3. Haz clic en el botón "Eliminar" para cualquier transacción para eliminarla de la lista.
	
4. Verifica que las transacciones se muestren correctamente.

::page{title="Ejercicios Prácticos"}

Los siguientes son algunos ejercicios prácticos para los aprendices interesados. No estamos proporcionando las soluciones para estos ejercicios para animar a los aprendices a intentar resolverlos por su cuenta. Siéntase libre de utilizar el foro de discusión del curso para compartir sus opiniones sobre la solución con otros aprendices interesados.

## Ejercicio 1: Buscar Transacciones
En este ejercicio, agregarás una nueva función a la aplicación que permite a los usuarios buscar transacciones dentro de un rango de cantidad especificado. Crearás una nueva ruta llamada `/search` que maneja tanto solicitudes `GET` como `POST` en `app.py`.
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0INQEN/search.gif" alt="Referencia de código correcto">

Instrucciones:
1. Crea una nueva función llamada `search_transactions` y utiliza el decorador `@app.route` para mapearla a la URL `/search`.

2. Dentro de la función, verifica si el método de solicitud es `POST`. Si lo es, recupera los valores mínimo y máximo de cantidad del formulario enviado por el usuario. Convierte estos valores a números de punto flotante.

3. Filtra la lista de transacciones en función del rango de cantidad especificado por el usuario. Crea una nueva lista, `filtered_transactions`, que contenga solo las transacciones cuyo monto se encuentre dentro del rango especificado. Puedes usar una comprensión de listas para esto.

4. Pasa la lista `filtered_transactions` a la plantilla `transactions.html` utilizando la función `render_template`. En esta plantilla, muestra las transacciones de manera similar a la plantilla existente `transactions.html`.

5. Si el método de solicitud es `GET`, renderiza una nueva plantilla llamada `search.html`. Esta plantilla debe contener un formulario que permita a los usuarios ingresar los valores de cantidad mínima y máxima para la búsqueda.

## Ejercicio 2: Saldo Total
En este ejercicio, agregarás una nueva función que calcula y muestra el saldo total de todas las transacciones. Crearás la ruta en `app.py`.
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0INQEN/balance.gif" alt="Referencia de código correcto">

Instrucciones:
1. Crea una nueva función llamada `total_balance` y utiliza el decorador `@app.route` para mapearla a la URL `/balance`.

2. Dentro de la función, calcula el saldo total sumando los valores de cantidad de todas las transacciones en la lista de transacciones.

3. Devuelve el saldo total como una cadena en el formato "Saldo Total: {balance}".

4. Para mostrar el saldo total, no necesitas crear una nueva plantilla. En su lugar, modificarás la plantilla `transactions.html` para incluir el valor del saldo total en la parte inferior de la tabla.

5. Después de mostrar la lista de transacciones en la plantilla `transactions.html`, agrega una nueva fila para mostrar el saldo total. Puedes usar la misma función `render_template` que antes, pasando tanto la lista de transacciones como el valor del saldo total.

::page{title="Conclusión"}

Felicidades por completar este laboratorio.

En este laboratorio, has aprendido a:
- Implementar funcionalidad CRUD en una aplicación de base de datos.
- Usar funciones adicionales de la biblioteca Flask para enrutamiento avanzado y gestión de solicitudes.
- Gestionar el enrutamiento entre múltiples archivos HTML según sea necesario.

## Author(s)

[Vicky Kuo](https://author.skills.network/instructors/vicky_kuo)

## Additional Contributor
[Abhishek Gagneja](https://author.skills.network/instructors/abhishek_gagneja "Abhishek Gagneja")
	
<!-- ## Changelog

| Date | Version | Changed by | Change Description |
|------|--------|--------|---------|
| 2023-07-24 | 2.0 | Steve Hord | QA pass with edits |
|2023-07-15 | 1.0 | Vicky Kuo | Initial version created |
|2026-04-03 | 3.0 | Rajashree Patil | Fix typo: transation → transaction in the hint block
Add return {"message": "Transaction not found"}, 404 to the final "Lab Help" code for consistency|
-->

## <h3 align="center"> &#169; IBM Corporation 2023. Todos los derechos reservados. <h3/> Este cuaderno y su código fuente se publican bajo los términos de la [Licencia MIT](https://cognitiveclass.ai/mit-license?cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ&cm_mmc=Email_Newsletter-_-Developer_Ed%2BTech-_-WW_WW-_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).