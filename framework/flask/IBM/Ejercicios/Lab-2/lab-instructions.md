::page{title="Laboratorio Práctico: Construcción y Despliegue de una Aplicación Web usando Flask"}

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0223EN-SkillsNetwork/images/IDSN-logo.png" width="200" alt="logo de cognitiveclass.ai">

## Introducción

En este laboratorio, creamos una aplicación básica de funciones matemáticas y la desplegamos a través de una interfaz web utilizando Flask. El propósito es conectar todas las piezas de conocimiento adquiridas en el curso hasta ahora y ver los pasos de desarrollo y despliegue de la aplicación en acción.

Tiempo estimado necesario: **30** minutos

## Objetivos

En esta tarea usted:

- Tarea 1: Crear las funciones matemáticas.
- Tarea 2: Empaquetar las funciones y probar el paquete.
- Tarea 3: Despliegue web del paquete de la aplicación utilizando Flask.

::page{title="Tarea 1: Escribir las funciones matemáticas"}

En esta tarea, se requiere que escribas un script que tenga funciones para sumar, restar y multiplicar dos valores. Llamemos a este script `mathematics.py`

Sigue los pasos para esta tarea.

1. Abre una ventana de terminal utilizando el menú en el editor: Terminal > Nueva Terminal.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0223EN-SkillsNetwork/images/new_terminal.png">

2. Ve al directorio principal del proyecto.

    ```bash
    cd /home/project
    ```
    

3. Ejecuta el siguiente comando para clonar el directorio del proyecto desde la URL de clonación que copiaste en el laboratorio de pretrabajo.

    ```bash
   git clone https://github.com/ibm-developer-skills-network/hjbsk-build_deploy_app_flask
    ```
    

4. Cambia al folder `practice_project`.

    ```bash
    cd /home/project/hjbsk-build_deploy_app_flask
    ```

5. Crea una carpeta llamada `Maths` y cámbiate a ese directorio.

    ```bash
    mkdir Maths
    cd Maths
    ```


6. En el explorador, ve al directorio `Maths` y crea un nuevo archivo llamado `mathematics.py`.

7. Agrega la función **summation** que toma `a` y `b` como argumentos numéricos, en `mathematics.py`.

<details>
<summary>Haz clic aquí para ver la solución</summary>
	
	```python
    def summation(a, b):
		result = a + b
        return result
    ```

</details>

8. Agrega la función **subtraction** que toma `a` y `b` como argumentos numéricos, en `mathematics.py`.

<details>
<summary>Haz clic aquí para ver la solución</summary>
	
	```python
    def subtraction(a, b):
		result = a - b
        return result
    ```

</details>

9. Agrega la función **multiplication** que toma `a` y `b` como argumentos numéricos, en `mathematics.py`.

<details>
<summary>Haz clic aquí para ver la solución</summary>
	
	```python
    def multiplication(a, b):
		result = a * b
        return result
    ```

</details>

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0223EN-SkillsNetwork/images/mathematics.png)

::page{title="__Tarea 2:__ Empaquetar las funciones"}

1. Crea el archivo `__init__.py` en el directorio `Maths`.

2. Importa el archivo `mathematics.py` al archivo `__init__.py`.

```python
from . import mathematics
```


3. Importa el paquete `Maths` en server.py.

```python
from Maths.mathematics import summation, subtraction, multiplication
```


4. En el server.py, para el punto final `/`, implementa un método que renderice el `index.html`.

```python
@app.route("/")
def render_index_page():
    return render_template('index.html')
```


5. En el espacio provisto en server.py para el endpoint `/sum`, implementa una función que utilice la función de suma apropiada del paquete que creaste en la parte anterior. La función debe recuperar `num1` y `num2` como entradas de tipo float de los parámetros de la solicitud. Luego, debe verificar si el resultado es un número entero utilizando el método `is_integer()`. Si lo es, convierte el resultado a un entero antes de devolverlo como una cadena.

6. En el espacio provisto en server.py para el endpoint `/sub`, implementa una función que utilice la función de resta apropiada del paquete que creaste en la parte anterior. La función debe recuperar `num1` y `num2` como entradas de tipo float de los parámetros de la solicitud. Luego, debe verificar si el resultado es un número entero utilizando el método `is_integer()`. Si lo es, convierte el resultado a un entero antes de devolverlo como una cadena.

7. En el espacio provisto en server.py para el endpoint `/mul`, implementa una función que utilice la función de multiplicación apropiada del paquete que creaste en la parte anterior. La función debe recuperar `num1` y `num2` como entradas de tipo float de los parámetros de la solicitud. Luego, debe verificar si el resultado es un número entero utilizando el método `is_integer()`. Si lo es, convierte el resultado a un entero antes de devolverlo como una cadena.

<!--![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0223EN-SkillsNetwork/images/server.png)-->

![Screenshot 2025-05-22 at 11.26.57 AM.png](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/_OYsOJ_wjUdCKD3hHWB6Rg/Screenshot%202025-05-22%20at%2011-26-57%E2%80%AFAM.png)

::page{title="__Tarea 3:__ Despliegue web del paquete de la aplicación utilizando Flask"}

1. Cambia el directorio actual en la terminal al directorio hjbsk-build_deploy_app_flask y ejecuta el servidor desde tu terminal.

```bash
cd /home/project/hjbsk-build_deploy_app_flask && python3.11 server.py
```


2. Verás que el servidor se inicia en el puerto 8080.

3. Haz clic en el `Skills Network button` a la izquierda, se abrirá el `Skills Network Toolbox`. Luego haz clic en `Other` y después en `Launch Application`. Desde allí deberías poder ingresar el número de puerto.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0223EN-SkillsNetwork/images/Launch%20app.png)

Conéctate al puerto `8080` y haz clic en el botón `Launch`.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0223EN-SkillsNetwork/images/launch%201.png)

4. Se abre una nueva ventana del navegador con la página de índice como se muestra a continuación.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0223EN-SkillsNetwork/images/Screenshot%20\(3720\).png)

Prueba tu aplicación para obtener los resultados deseados. Algunos ejemplos se muestran a continuación.

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0223EN-SkillsNetwork/images/add.png)

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0223EN-SkillsNetwork/images/sub.png)

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0223EN-SkillsNetwork/images/mul.png)

::page{title="(Opcional) Ejercicio de práctica"}

Los estudiantes interesados pueden intentar incorporar la capacidad de manejo de errores en esta aplicación desplegada. Por ejemplo, en caso de que la interfaz reciba entradas no numéricas para operaciones matemáticas, ¿cuál debería ser la respuesta del sistema?

::page{title="Conclusión"}

¡Felicidades! Has completado las tareas para este proyecto.

Al final de este laboratorio, has:

1. Creado funciones que realizan operaciones matemáticas.

2. Creado un paquete para estas funciones.

3. Desplegado la aplicación que utiliza este paquete en localhost usando Flask.



## Authors

Shivam

## Change Log

| Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
| ----------------- | ------- | ----------------- | ---------------------------------- |
| 2025-05-22 | 1.2| Ritika Joshi | Modified the instructions as part of Content Analysis|
| 2023-07-13 | 1.1 | Abhishek Gagneja | Modified the instruction set|
| 2023-06-28        | 1.0     | Shivam | Created initial version of the lab |

 ## <h3 align="center"> &#169; IBM Corporation 2023. Todos los derechos reservados. <h3/>