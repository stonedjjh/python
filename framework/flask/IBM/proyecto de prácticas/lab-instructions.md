::page{title="Desarrollo y despliegue de aplicaciones web basadas en IA"}

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0224EN-Coursera/images/IDSN-logo.png" width="200"> <br>

Tiempo estimado: 60 minutos

## Descripción general
En este proyecto, utilizamos las bibliotecas de IA de Watson integradas para crear una aplicación que realice análisis de sentimientos en un texto proporcionado. Luego, desplegamos dicha aplicación en la web utilizando el framework Flask.

## Directrices del proyecto

Para completar este proyecto, deberás realizar las siguientes 8 tareas, basadas en el conocimiento que has adquirido a través del curso.

## Tareas y objetivos:
- Tarea 1: Clonar el repositorio del proyecto
- Tarea 2: Crear una aplicación de análisis de sentimientos utilizando la biblioteca NLP de Watson
- Tarea 3: Formatear la salida de la aplicación
- Tarea 4: Empaquetar la aplicación
- Tarea 5: Ejecutar pruebas unitarias en tu aplicación
- Tarea 6: Desplegar como aplicación web utilizando Flask
- Tarea 7: Incorporar manejo de errores
- Tarea 8: Ejecutar análisis de código estático

¡Comencemos!

::page{title="Acerca de las bibliotecas de IA de Watson embebibles"}

En este proyecto, utilizarás bibliotecas embebibles para crear una aplicación de Python potenciada por IA.

[Bibliotecas de IA de Watson embebibles](https://developer.ibm.com/articles/watson-libraries-embeddable-ai-that-works-for-you "Bibliotecas de IA de Watson embebibles") incluyen la biblioteca de NLP, la biblioteca de texto a voz y la biblioteca de voz a texto. Estas bibliotecas pueden ser embebidas y distribuidas como parte de tu aplicación. Para tu conveniencia, estas bibliotecas ya están preinstaladas en Skills Network Labs Cloud IDE para su uso en este proyecto.

La biblioteca de NLP incluye funciones para análisis de sentimientos, detección de emociones, clasificación de texto, detección de idiomas, etc. entre otras. La biblioteca de voz a texto contiene funciones que realizan el servicio de transcripción y generan texto escrito a partir de audio hablado. La biblioteca de texto a voz genera audio con sonido natural a partir de texto escrito.

> **Por favor, ejecuta este laboratorio en el **entorno de Skills Network Theia Lab** en sí, no en tu IDE local (como VS Code). La API utilizada aquí está alojada en la plataforma Skills Network y solo es accesible dentro del Theia Lab.**

::page{title="Tarea 1: Clonar el repositorio del proyecto"}

El repositorio de Github del proyecto está disponible en la URL mencionada a continuación.

```bash
https://github.com/ibm-developer-skills-network/zzrjt-practice-project-emb-ai.git
```


*Puedes encontrar instrucciones sobre cómo bifurcar el repositorio visitando el ejercicio 2 en este [Laboratorio Práctico: Familiarízate con los comandos de Git](https://cf-courses-data.static.labs.skills.network/9Yqz09lYagTH_Eo5c9BXqQ/Get%20familiar%20con%20los%20comandos%20de%20Git-v1.md.html).*

>Nota: Asegúrate de que tu repositorio bifurcado sea público.

1. Abre una nueva Terminal y crea el directorio `practice_project` usando el comando mkdir y cambia el directorio actual a `practice_project` usando el comando `c&#8203;d`.

```
mkdir practice_project
cd practice_project
```


2. Clona este repositorio de GitHub bifurcado utilizando la terminal de Cloud IDE a tu proyecto en una carpeta llamada `practice_project`.
*Puedes encontrar instrucciones sobre cómo obtener la URL de clonación del repositorio visitando el ejercicio 3 en este [Laboratorio práctico: Familiarízate con los comandos de Git](https://cf-courses-data.static.labs.skills.network/9Yqz09lYagTH_Eo5c9BXqQ/Get%20familiar%20con%20los%20comandos%20de%20Git-v1.md.html).*
<details>
<summary>Haz clic aquí para obtener una pista</summary>

```  
git clone <Paste_URL_here> folder
```


</details>
<details>
<summary>Haga clic aquí para la solución</summary>
  


```
  git clone https://github.com/ibm-developer-skills-network/zzrjt-practice-project-emb-ai.git practice_project
```


>Nota: Asegúrate de usar la URL de tu propio repositorio bifurcado.
</details>

4. Después de que se complete la clonación, usa la terminal para cambiar el directorio actual `practice_project` utilizando el comando `c&#8203;d`.

- Asegúrate de que Python 3.11 y las bibliotecas requeridas estén disponibles:
     ```bash
     python3.11 -V
     pip3.11 show requests flask pylint
     ```
 - Instala las bibliotecas que falten:
     ```bash
     python3.11 -m pip install requests flask pylint
     ```

- Al finalizar, la pestaña del proyecto debería tener la estructura de carpetas como se muestra en la imagen.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0224EN-Coursera/images/git_clone.png">

::page{title="Tarea 2: Crear una aplicación de análisis de sentimientos utilizando la biblioteca Watson NLP"}

El análisis de sentimientos en NLP es la práctica de utilizar computadoras para reconocer el sentimiento o la emoción expresada en un texto. A través de NLP, el análisis de sentimientos categoriza las palabras como positivas, negativas o neutrales.

El análisis de sentimientos se realiza a menudo en datos textuales para ayudar a las empresas a monitorear el sentimiento de marca y producto en la retroalimentación de los clientes, y comprender las necesidades del cliente. Ayuda a captar la actitud y el estado de ánimo del público en general, lo que puede ayudar a recopilar información valiosa sobre el contexto.

Para crear la aplicación de análisis de sentimientos, utilizaremos las Bibliotecas de IA Embebida de Watson. Dado que las funciones de estas bibliotecas ya están desplegadas en el servidor Cloud IDE, no es necesario importar estas bibliotecas a nuestro código. En su lugar, necesitamos enviar una solicitud POST al modelo relevante con el texto requerido y el modelo enviará la respuesta apropiada.

Un código de muestra para tal aplicación podría ser

```python
import requests

def <function_name>(<input_args>):
	url = '<relevant_url>'
	headers = {<header_dictionary>}
	myobj = {<input_dictionary_to_the_function>}
	response = requests.post(url, json = myobj, headers=header)
    return response.text
```


*Nota: La respuesta de las funciones de NLP de Watson es en forma de objeto. Para acceder a los detalles de la respuesta, podemos usar el atributo `text` del objeto llamando a `response.text` y hacer que la función devuelva la respuesta como texto simple.*

Para este proyecto, utilizarás la función de Análisis de Sentimientos basada en BERT de la Biblioteca NLP de Watson. Para acceder a esta función, la URL, los encabezados y el formato json de entrada son los siguientes.

```
URL: 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
Headers: {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
Input json: { "raw_document": { "text": text_to_analyse } }
```


Aquí, `text_to_analyze` se está utilizando como una variable que contiene el texto escrito que se va a analizar.

En esta tarea, necesitas crear un nuevo archivo llamado `sentiment_analysis.py` en la carpeta `practice_project`. En este archivo, escribe la función para ejecutar el análisis de sentimientos utilizando la función de Análisis de Sentimientos de Watson NLP BERT, como se discutió anteriormente. Llamaremos a esta función `sentiment_analyzer`. Supón que el texto a analizar se pasa a la función como un argumento y se almacena en la variable `text_to_analyse`.

<details>
<summary>Haz clic aquí para la solución</summary>
sentiment_analysis.py	
	
	import requests  # Importar la biblioteca requests para manejar solicitudes HTTP

	def sentiment_analyzer(text_to_analyse):  # Definir una función llamada sentiment_analyzer que toma una entrada de tipo cadena (text_to_analyse)
		url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'  # URL del servicio de análisis de sentimientos
		myobj = { "raw_document": { "text": text_to_analyse } }  # Crear un diccionario con el texto a analizar
		header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}  # Establecer las cabeceras requeridas para la solicitud API
		response = requests.post(url, json = myobj, headers=header)  # Enviar una solicitud POST a la API con el texto y las cabeceras
		return response.text  # Devolver el texto de la respuesta de la API

	
</details>

Esta aplicación ahora se puede llamar utilizando el shell de Python. Para probar la aplicación, abre un shell de Python usando python3.11 para abrir el shell de Python en el directorio actual, es decir, practice_project. *Asegúrate de que el directorio actual sea `practice_project`.*

```bash
python3.11
```


En el shell de Python, importa la función `sentiment_analyzer`.
<details>
<summary>Haz clic aquí para obtener una pista</summary>
Sintaxis:
	
	from file_name import function_name
	
</details>

<details>
<summary>Haz clic aquí para ver la solución</summary>
	
	from sentiment_analysis import sentiment_analyzer
	
</details>

Después de la importación exitosa, prueba tu aplicación con el texto "Me encanta esta nueva tecnología."

```bash
sentiment_analyzer("I love this new technology")
```


El resultado esperado es el que se muestra en la imagen a continuación. Para salir del shell de python, presiona `Ctrl+Z` o escribe `exit()`.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0224EN-Coursera/images/senti_response.png">

Esto completa la Tarea 2. Ten en cuenta que en la salida, la información relevante para nosotros es solo la `label` y el `score`. En la siguiente tarea, extraerás esta información de esta salida.

::page{title="Tarea 3: Formatear la salida de la aplicación"}

La salida de la aplicación creada está en forma de un diccionario, pero ha sido formateada como texto. Para acceder a piezas relevantes de información de esta salida, primero necesitamos convertir este texto en un diccionario. Dado que los diccionarios son el sistema de formato predeterminado para archivos JSON, utilizamos la biblioteca incorporada de Python `json`.

Veamos cómo funciona esto.

Primero, en un shell de Python, importa la biblioteca json.

```python
import json
```


A continuación, ejecuta la función sentiment_analyzer para el texto "I love this new technology", tal como en la Tarea 2, y almacena la salida en una variable llamada `response`.

```python
from sentiment_analysis import sentiment_analyzer
response = sentiment_analyzer("I love this new technology")
```


Ahora, pasa la variable `response` como un argumento a la función json.loads y guarda la salida en `formatted_response`. Imprime `formatted_response` para ver la diferencia en el formato.

```python
formatted_response = json.loads(response)
print(formatted_response)
```


La salida esperada de los pasos mencionados anteriormente se muestra en la imagen a continuación.
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0224EN-Coursera/images/jsonify.png">

Tenga en cuenta que la ausencia de comillas simples a cada lado de la respuesta indica que esto ya no es un texto, sino que es un diccionario. Para acceder a la información correcta de este diccionario, necesitamos acceder a las claves de manera apropiada. Dado que esta es una estructura de diccionario anidado, es decir, un diccionario de diccionarios, se deben utilizar las siguientes declaraciones para obtener las salidas de etiqueta y puntuación de esta respuesta.

```python
label = formatted_response['documentSentiment']['label']
score = formatted_response['documentSentiment']['score']
```


Verifica el contenido de `label` y `score` para comprobar la salida.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0224EN-Coursera/images/jsonify_check.png">

Ahora, para la Tarea 3, incorpora la técnica mencionada anteriormente y realiza cambios en el archivo `sentiment_analysis.py`. La salida esperada al llamar a la función `sentiment_analyzer` debería ser ahora un diccionario con 2 claves, label y score, cada una con el valor apropiado extraído de la respuesta de la función NLP de Watson. Verifica tus cambios probando la función modificada en un shell de python.

<details>
<summary>Haz clic aquí para la solución</summary>
	
	import requests
    import json

	def sentiment_analyzer(text_to_analyse):
		# URL del servicio de análisis de sentimientos
		url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

		# Construyendo la carga útil de la solicitud en el formato esperado
		myobj = { "raw_document": { "text": text_to_analyse } }

		# Encabezado personalizado especificando el ID del modelo para el servicio de análisis de sentimientos
		header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

		# Enviando una solicitud POST a la API de análisis de sentimientos
		response = requests.post(url, json=myobj, headers=header)

		# Analizando la respuesta JSON de la API
		formatted_response = json.loads(response.text)

		# Extrayendo la etiqueta de sentimiento y la puntuación de la respuesta
		label = formatted_response['documentSentiment']['label']
		score = formatted_response['documentSentiment']['score']

		# Devolviendo un diccionario que contiene los resultados del análisis de sentimientos
		return {'label': label, 'score': score}

	
</details>

Al finalizar, la salida esperada de la función se muestra en la imagen a continuación.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0224EN-Coursera/images/jsonify_test.png">

Para salir del shell de python, escribe `exit()` o presiona `Ctrl+Z`.

::page{title="Tarea 4: Empaquetar la aplicación"}

En esta tarea, debes empaquetar la aplicación final que creaste en las tareas 2 y 3.

Mantendremos el nombre del paquete como `SentimentAnalysis`. Los pasos involucrados en el empaquetado son:
1. Crea una carpeta en el directorio de trabajo, con el nombre como el nombre del paquete.
	
<details>
<summary>Haz clic aquí para obtener una pista</summary>
mkdir <package_name>
</details>
<details>
<summary>Haz clic aquí para ver la solución</summary>
	
	
	mkdir SentimentAnalysis
	
	
</details>

2. Mueve el código de la aplicación (es decir, el módulo) a la carpeta del paquete.
	
<details>
<summary>Haz clic aquí para obtener una pista</summary>
Puedes usar un comando de terminal o la consola de Cloud IDE para mover el archivo `sentiment_analysis.py` a la carpeta `SentimentAnalysis`.
</details>
<details>
<summary>Haz clic aquí para ver la solución</summary>
	
	
	mv ./sentiment_analysis.py ./SentimentAnalysis
	
	
</details>

3. Crea el nuevo archivo como \_\_init\_\_.py dentro de la carpeta del paquete para referenciar el módulo.

<details>
<summary>Haz clic aquí para obtener una pista</summary>
Importa el módulo/función de la carpeta actual en el archivo init.
</details>
<details>
<summary>Haz clic aquí para ver la solución</summary>
Inserta esta línea en __init__.py	
	
	from . import sentiment_analysis
	
	
</details>

La estructura final de la carpeta debería verse como se muestra en la imagen a continuación.
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0224EN-Coursera/images/packaging.png" width="300">

`SentimentAnalysis` es ahora un paquete válido y puede ser importado en cualquier archivo de este proyecto.

Para probar esto, ejecuta un shell de python en la terminal e intenta importar la función `sentiment_analyzer` del paquete.

<details>
<summary>Haz clic aquí para obtener una pista</summary>
La sintaxis para esta importación es 
	
	from package_name.module_name import function_name
	
</details>
<details>
<summary>Haz clic aquí para ver la solución</summary>
	
	from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
	
</details>

No recibir un mensaje de error después de la declaración de importación indicaría que el paquete ahora está listo para su uso. Prueba la función ejecutando la siguiente declaración en el shell.

```
sentiment_analyzer("This is fun.")
```


La salida recibida se vería como se muestra a continuación.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0224EN-Coursera/images/packaging_2.png" width="300">

Para salir del shell de python, escribe `exit()` o presiona `Ctrl+Z`.

::page{title="Tarea 5: Ejecutar pruebas unitarias en tu aplicación"}

Dado que ahora tenemos una aplicación funcional, es necesario que ejecutemos pruebas unitarias en algunos casos de prueba para verificar la validez de sus salidas.

Para ejecutar pruebas unitarias, necesitamos crear un nuevo archivo que llame a la función de aplicación requerida desde el paquete y la pruebe con un par de texto y salida conocidos.

Para ello, completa los siguientes pasos.
1. Crea un nuevo archivo en la carpeta `practice_project`, llamado `test_sentiment_analysis.py`.
	
2. En este archivo, importa la función `sentiment_analyzer` del paquete `SentimentAnalysis`. También importa la biblioteca `unittest`.
	
<details>
<summary>Haz clic aquí para la solución</summary>
	
    
	from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
    import unittest
	
	
</details>

3. Crea la clase de prueba unitaria. Llamémosla TestSentimentAnalyzer. Define `test_sentiment_analyzer` como la función para ejecutar las pruebas unitarias.

<details>
<summary>Haz clic aquí para la solución</summary>
	
    
	class TestSentimentAnalyzer(unittest.TestCase):
		def test_sentiment_analyzer(self):
	
	
</details>

4. Define 3 pruebas unitarias en la función mencionada y verifica la validez de los siguientes pares de enunciado - etiqueta.
	"I love working with Python": "SENT_POSITIVE"
	"I hate working with Python": "SENT_NEGATIVE"
	"I am neutral on Python": "SENT_NEUTRAL"

<details>
<summary>Haz clic aquí para una pista</summary>
Usa la función `assertEqual` para comparar la `etiqueta` de la salida con la etiqueta esperada.
</details>
<details>
<summary>Haz clic aquí para la solución</summary>
	
	
	class TestSentimentAnalyzer(unittest.TestCase):
		def test_sentiment_analyzer(self):
        	# Caso de prueba para sentimiento positivo
        	result_1 = sentiment_analyzer('I love working with Python')
        	self.assertEqual(result_1['label'], 'SENT_POSITIVE')
        	# Caso de prueba para sentimiento negativo
        	result_2 = sentiment_analyzer('I hate working with Python')
        	self.assertEqual(result_2['label'], 'SENT_NEGATIVE')
        	# Caso de prueba para sentimiento neutral
        	result_3 = sentiment_analyzer('I am neutral on Python')
        	self.assertEqual(result_3['label'], 'SENT_NEUTRAL')

	
</details>

5. Llama a las pruebas unitarias.

<details>
<summary>Haz clic aquí para la solución</summary>
Agrega la siguiente línea al final del archivo.
    
	unittest.main()
	
	
</details>

Ahora que el archivo está listo, ejecuta el archivo para realizar las pruebas unitarias. Tras una ejecución exitosa, la salida de este archivo debería ser como se muestra en la imagen a continuación.
	
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0224EN-Coursera/images/unittesting.png">

::page{title="Tarea 6: Desplegar como aplicación web usando Flask"}

Ahora que la aplicación está lista, es momento de desplegarla para su uso a través de una interfaz web. Para facilitar el proceso de despliegue, se te han proporcionado 3 archivos que se utilizarán para esta tarea.
 - Verifica la estructura del directorio:
  ```
  practice_project/
  ├── SentimentAnalysis/
  │   ├── __init__.py
  │   ├── sentiment_analysis.py
  ├── templates/
  │   ├── index.html
  ├── static/
  │   ├── mywebscript.js
  ├── server.py
  ```

- Este `index.html` en la carpeta `templates` contiene el código para la interfaz web que ha sido diseñada para este laboratorio. Se te proporciona tal cual y se debe usar sin modificaciones. No se requiere que realices ningún cambio en este archivo.

La interfaz es como se muestra en la imagen.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0224EN-Coursera/images/web_interface.png">
	
- Al hacer clic en el botón `Run Sentiment Analysis` en la interfaz html, se llama a este archivo mywebscript.js en la carpeta `static`, que ejecuta una solicitud GET y toma el texto proporcionado por el usuario como entrada. Este texto, guardado en una variable llamada `textToAnalyze`, se pasa al archivo del servidor para ser enviado a la aplicación. Este archivo también se te proporciona tal cual y se espera que se use sin modificaciones. No se requiere que realices ningún cambio en este archivo.

- Abre `server.py` en la carpeta `practice_project`. Esta tarea gira en torno a la finalización de este archivo. Puedes completar este archivo siguiendo los siguientes 5 pasos.

a. *Importar las bibliotecas y funciones relevantes*
	
En este archivo, necesitarás la biblioteca Flask junto con su función `render_template` (para desplegar el archivo HTML) y la función `request` (para iniciar la solicitud GET desde la página web).

También necesitarás importar la función `sentiment_analyzer` del paquete `SentimentAnalysis`.

Agrega las líneas de código relevantes, importando las funciones mencionadas, en `server.py`

<details>
<summary>Haz clic aquí para ver la solución</summary>
    
	from flask import Flask, render_template, request
    from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
	
</details>

b. *Iniciar la aplicación Flask con el nombre `Sentiment Analyzer`*

Aplica el conocimiento adquirido en el Módulo 2 de este curso y agrega la declaración a server.py que inicia la aplicación y la nombra `Sentiment Analyzer`.

<details>
<summary>Haz clic aquí para ver la solución</summary>
	
	app = Flask("Sentiment Analyzer")
	
</details>

c. *Definir la función `sent_analyzer`*

El propósito de esta función es doble. Primero, la función debe enviar una solicitud GET a la interfaz HTML para recibir el texto de entrada. Ten en cuenta que la solicitud GET debe hacer referencia a la variable `textToAnalyze` como se define en el archivo `mywebscript.js`. Almacena el texto entrante en una variable `text_to_analyze`. Ahora, como segundo paso, llama a tu aplicación `sentiment_analyzer` con `text_to_analyze` como argumento.

Además, formatea la salida de retorno de la función en un texto formal. Por ejemplo:
`El texto proporcionado ha sido identificado como POSITIVO con un puntaje de 0.99765.`
<details>
<summary>Haz clic aquí para ver una pista</summary>

1. Usa request.args.get para iniciar la solicitud GET.
2. La etiqueta, recibida como "SENT_CLASS" (donde la clase puede ser POSITIVO, NEGATIVO o NEUTRAL), deberá dividirse en '_' para acceder al nombre de la clase individualmente.
</details>
<details>
<summary>Haz clic aquí para ver la solución</summary>
La función debería verse así.
	
	```python
	@app.route("/sentimentAnalyzer")
	def sent_analyzer():
		# Recuperar el texto a analizar de los argumentos de la solicitud
		text_to_analyze = request.args.get('textToAnalyze')

		# Pasar el texto a la función sentiment_analyzer y almacenar la respuesta
		response = sentiment_analyzer(text_to_analyze)

		# Extraer la etiqueta y el puntaje de la respuesta
		label = response['label']
		score = response['score']

		# Devolver una cadena formateada con la etiqueta de sentimiento y el puntaje
		return "El texto proporcionado ha sido identificado como {} con un puntaje de {}.".format(label.split('_')[1], score)

	```
	
</details>

Nota: La función utiliza el decorador de Flask `@app.route("/sentimentAnalyzer")` como se hace referencia en el archivo `mywebscript.js`.

d. *Renderizar la plantilla HTML usando `render_index_page`*

Esta función simplemente debe ejecutar la función render_template sobre la plantilla HTML, `index.html`.

<details>
<summary>Haz clic aquí para ver la solución</summary>
	
	@app.route("/")
    def render_index_page():
        return render_template('index.html')

</details>

e. *Ejecutar la aplicación en `localhost:5000`*

Finalmente, al ejecutar el archivo, ejecuta la aplicación en el host: `0.0.0.0` (o localhost) en el número de puerto 5000.
<details>
<summary>Haz clic aquí para ver la solución</summary>

```python	
	if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)
```	


</details>

Para desplegar la aplicación, ejecuta el archivo *server.py* desde la terminal.

```bash
python3.11 server.py
```


La salida se vería así.
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0224EN-Coursera/images/falsk_deploy.png">

La aplicación ahora está en funcionamiento en localhost:5000. Para acceder a la aplicación, ve a la pestaña del Skills Network Toolbox y haz clic en Lanzar Aplicación. Ingresa el puerto de la Aplicación como 5000 y haz clic en Tu Aplicación.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0224EN-Coursera/images/app_deploy.png">

La interfaz de la aplicación se abrirá. Utiliza la interfaz para probar tu aplicación.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0224EN-Coursera/images/final_deploymen.png">

Para detener la aplicación, presiona `Ctrl+C`.

::page{title="Tarea 7: Incorporar manejo de errores"}

Para incorporar el manejo de errores, necesitamos identificar las diferentes formas de códigos de error que pueden ser recibidos en respuesta a la consulta GET iniciada por la función `sent_analyzer` en `server.py`.

Esto ya es parte de las funciones de la Biblioteca Watson NLP y se puede observar en la consola del terminal donde se está ejecutando el código.

Considera la imagen mostrada a continuación.
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0224EN-Coursera/images/error_handling.png">

Los códigos indican que la solicitud GET inicial fue exitosa (200), la solicitud fue devuelta como No Modificada desde la caché (304) y luego la solicitud GET para generar la respuesta también se realizó con éxito.

En el caso de entradas inválidas, el sistema responde con el código de error 500, indicando que hay algo mal en el servidor. Una entrada inválida podría ser cualquier cosa que el modelo no pueda interpretar. Sin embargo, en la situación de este error, la salida de esta aplicación no se actualiza.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0224EN-Coursera/images/Error_handling_1.png">

Ten en cuenta que la salida en la interfaz es la misma que antes, el texto que se está analizando es un texto aleatorio y las bibliotecas de IA de Watson están generando un error 500, confirmando que el modelo no ha podido procesar la solicitud.

Para corregir este error en nuestra aplicación, necesitamos estudiar la respuesta recibida de la función de la biblioteca de IA de Watson, cuando el servidor genera un error 500. Para probar esto, necesitamos retroceder los pasos tomados en la Tarea 2 y probar la biblioteca de IA de Watson con una entrada de cadena inválida.

Abre un shell de Python en el terminal y ejecuta los siguientes comandos para verificar la salida requerida después de actualizar el archivo sentiment_analysis.py con lo siguiente.

```python
	
import requests

# Define the URL for the sentiment analysis API
url = "https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"

# Set the headers with the required model ID for the API
headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

# Define the first payload with nonsensical text to test the API
myobj = { "raw_document": { "text": "as987da-6s2d aweadsa" } }

# Make a POST request to the API with the first payload and headers
response = requests.post(url, json=myobj, headers=headers)

# Print the status code of the first response
print(response.status_code)

# Define the second payload with a meaningful text to test the API
myobj = { "raw_document": { "text": "Testing this application for error handling" } }

# Make a POST request to the API with the second payload and headers
response = requests.post(url, json=myobj, headers=headers)

# Print the status code of the second response
print(response.status_code)
 
```


La respuesta de la consola se ve como se muestra en la imagen a continuación. Las cajas rojas indican el texto inválido y su código de estado recibido, y las cajas amarillas indican el texto válido y su código de estado recibido.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0224EN-Coursera/images/Error_handling_2.png">

Esto te permite modificar la aplicación de tal manera que podamos enviar diferentes salidas para diferentes códigos de estado.

En la primera parte de esta tarea, debes modificar la función `sentiment_analyzer()` para que devuelva tanto `label` como `score` como `None` en caso de entrada de texto inválida.

<details>
<summary>Haz clic aquí para obtener una pista</summary>
Haz una declaración condicional if-else en la función sentiment_analyzer para agregar la funcionalidad necesaria.
</details>

<details>
<summary>Haz clic aquí para ver la solución</summary>
sentiment_analysis.py

```python 
	import requests
    import json

	def sentiment_analyzer(text_to_analyze):
		# Define the URL for the sentiment analysis API
		url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

		# Create the payload with the text to be analyzed
		myobj = { "raw_document": { "text": text_to_analyze } }

		# Set the headers with the required model ID for the API
		header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

		# Make a POST request to the API with the payload and headers
		response = requests.post(url, json=myobj, headers=header)

		# If the response status code is 200, extract the label and score from the response
		if response.status_code == 200:
			# Parse the response from the API
			formatted_response = json.loads(response.text)
			label = formatted_response['documentSentiment']['label']
			score = formatted_response['documentSentiment']['score']
		# If the response status code is 500, set label and score to None
		elif response.status_code == 500:
			label = None
			score = None
		# For any other unexpected status codes, set label and score to None
		else:
			label = None
			score = None

		# Return the label and score in a dictionary
		return {'label': label, 'score': score}
```


</details>

Ahora, en `server.py`, la respuesta que se enviará a la consola también debe ser diferente para los tipos de entrada válidos e inválidos. Para una entrada inválida, deja que la consola imprima `¡Entrada inválida! Intenta de nuevo.`

<details>
<summary>Haz clic aquí para obtener una pista</summary>
Crea una declaración condicional if-else en la función sent_analyzer de server.py para verificar si "label" es None o no.
</details>

<details>
<summary>Haz clic aquí para la solución</summary>

```python 
	def sent_analyzer():
		# Retrieve the text to analyze from the request arguments
		text_to_analyze = request.args.get('textToAnalyze')

		# Pass the text to the sentiment_analyzer function and store the response
		response = sentiment_analyzer(text_to_analyze)

		# Extract the label and score from the response
		label = response['label']
		score = response['score']

		# Check if the label is None, indicating an error or invalid input
		if label is None:
			return "Invalid input! Try again."
		else:
			# Return a formatted string with the sentiment label and score
			return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)
```


</details>

Ahora, tu aplicación es capaz de responder adecuadamente a cualquier forma de entrada.
<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0224EN-Coursera/images/Error_handling_3.png">

::page{title="Tarea 8: Ejecutar análisis de código estático"}

Finalmente, en la Tarea 8, verificamos la calidad de tus habilidades de codificación según las pautas PEP8 mediante la ejecución de un análisis de código estático.

Normalmente, esto se realiza en el momento de empaquetar y realizar pruebas unitarias de la aplicación. Sin embargo, hemos mantenido este paso al final de este proyecto ya que los códigos se actualizaron en todas las tareas anteriores. Una vez que tus archivos para este proyecto estén listos, probemos su adherencia a las pautas PEP8.

Dado que `PyLint` ya estaba instalado en la Tarea 1, puedes proceder directamente a ejecutar el análisis. Si por alguna razón no está disponible en tu entorno, puedes instalarlo usando la terminal.

<details>
<summary>Haz clic aquí para la solución</summary>
	
	python3.11 -m pip install pylint
	
</details>

A continuación, utiliza pylint para ejecutar el análisis de código estático en `server.py`.
<details>
<summary>Haz clic aquí para la solución</summary>
En la terminal bash ejecuta el siguiente comando.
	
	pylint server.py
	
</details>

Si todos los aspectos de la guía PEP8 han sido incorporados en tu código, entonces la puntuación generada debería ser 10/10. En caso de que no lo sea, sigue las instrucciones proporcionadas por la biblioteca pylint para modificar el código adecuadamente.

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0224EN-Coursera/images/static_code_analysis.png">

Esto concluye el proyecto práctico.

::page{title="(Opcional) Ejercicios Adicionales"}

Los aprendices interesados pueden intentar los siguientes ejercicios por su cuenta, para una mejor comprensión de los conceptos aprendidos a través de este proyecto. No se proporciona solución para estos ejercicios. Sin embargo, siéntete libre de discutir y compartir tus soluciones con tus compañeros en los foros de discusión del curso.

1. Realiza un análisis de código estático en `sentiment_analysis.py`. Intenta lograr una puntuación de 10/10. Sugerencia: *Docstrings*

2. Prueba la capacidad de tu aplicación para manejar oraciones en idiomas distintos al inglés, por ejemplo, francés, alemán, etc. Verifica si la aplicación responde con un error de texto inválido.

3. Actualmente, si la aplicación se ejecuta SIN proporcionar una entrada, es decir, dejando el texto en blanco, el modelo aún arroja el mismo error de texto inválido. Intenta incluir un caso especial, donde una entrada en blanco reciba un mensaje de error diferente.

::page{title="Conclusión"}

Felicitaciones por completar este proyecto.

Con la finalización de este proyecto, has:

1. Creado una aplicación de análisis de sentimientos basada en IA utilizando las bibliotecas integradas de Watson NLP.

2. Formateado la salida recibida de la función de la biblioteca Watson NLP para extraer información relevante de ella.

3. Empaquetado la aplicación y la has hecho importable a cualquier código Python para su uso.

4. Ejecutado pruebas unitarias en la aplicación y verificado la validez de sus salidas para diferentes entradas.

5. Desplegado la aplicación utilizando el marco Flask.

6. Incorporado la capacidad de manejo de errores en la aplicación, de modo que un código de respuesta 500 reciba una respuesta apropiada de la aplicación.

7. Ejecutado un análisis de código estático en los archivos de código para confirmar su adherencia a las pautas PEP8.
	
<!--## Author(s)
Abhishek Gagneja

## Changelog
| Date | Version | Changed by | Change Description |
|------|--------|--------|---------|
|2026-04-09 | 1.5 | Ritika Joshi | Added hints for git instructions and corrected Task 7 & 8 |
|2025-05-20 | 1.4 | Ritika Joshi | updated the instructions as part of GA |
|2023-08-29 | 1.3 | Ritika Joshi | updated the instructions |
|2023-07-11 | 1.2 | Abhishek Gagneja | Added new functionalities |
|2023-07-10 | 1.1 | Abhishek Gagneja | Changes in instructions and images|
|2023-06-30 | 1.0 | Abhishek Gagneja | Initial version created |-->
	
	
## <h3 align="center"> &#169; IBM Corporation 2023. Todos los derechos reservados. <h3/>