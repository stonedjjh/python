# Gradio

Gradio permite mostrar y evaluar modelos de aprendizaje automático mediante una interfaz web fácil de usar que puede ser accedida desde cualquier lugar. Es un paquete de Python de código abierto diseñado para construir rápidamente demostraciones o aplicaciones web para modelos de aprendizaje automático, APIs o cualquier función arbitraria de Python. Posteriormente, se puede compartir un enlace a la demostración o aplicación web utilizando las funciones integradas para compartir de Gradio. No se requiere experiencia previa en JavaScript, CSS ni alojamiento web.

## ¿Por qué usar Gradio?

Gradio es útil por varias razones:

- **Facilidad de uso:** Gradio permite la creación de interfaces para modelos con solo unas pocas líneas de código.
- **Flexibilidad:** Gradio admite diversas entradas y salidas, como texto, imágenes, archivos y más.
- **Compartir y colaborar:** Las interfaces se pueden compartir con otros a través de URL únicas, facilitando la colaboración y la recopilación de comentarios.

### Tarea 

1. **Comenzando con Gradio**
   Para comenzar a utilizar Gradio, primero se debe instalar la biblioteca a través de pip:

   ```bash
   pip install gradio
   ```

2. **Creando la primera interfaz de Gradio**
   Gradio puede ejecutarse en cualquier editor de código, Jupyter Notebook, Google Colab o entorno de ejecución de Python. A continuación se presenta el código para escribir una primera aplicación de Gradio:

   ```PYTHON
   import gradio as gr
   def greet(name, intensity):
     return "Hello, " + name + "!" * int(intensity)
   demo = gr.Interface(
     fn=greet,
     inputs=["text", "slider"],
     outputs=["text"],
   )
   demo.launch(server_name="127.0.0.1", server_port= 7860)
   ```

   Si el código se ejecuta desde un archivo, la demostración se abrirá en un navegador web en la dirección http://127.0.0.1:7860. Si se ejecuta dentro de un cuaderno (notebook), la demostración se mostrará incrustada en él.

3. **Prueba de funcionamiento**
   Al ingresar un nombre en el cuadro de texto de la izquierda, arrastrar el control deslizante y presionar el botón de enviar, se mostrará un saludo personalizado en el panel de la derecha.

### Entendiendo la clase Interface

> [!NOTE]
> Para realizar la primera demostración, se debe crear una instancia de la clase `gr.Interface`. La clase `Interface` está diseñada para construir demostraciones de modelos de aprendizaje automático que aceptan una o más entradas y devuelven una o más salidas.

La clase Interface tiene tres argumentos principales:

- **fn:** La función que se desea envolver en una interfaz de usuario (UI).
- **inputs:** El o los componentes de Gradio que se utilizarán para recibir los datos de entrada. El número de componentes debe coincidir con la cantidad de argumentos de la función especificada en `fn`.
- **outputs:** El o los componentes de Gradio que se utilizarán para mostrar los resultados de salida. El número de componentes debe coincidir con la cantidad de valores de retorno de la función.

El argumento **fn** es flexible: se puede pasar cualquier función de Python que se desee envolver con una interfaz de usuario. En el ejemplo anterior se utilizó una función simple, pero la función puede ser tan compleja como un generador de música, una calculadora de impuestos o la función de predicción de un modelo de aprendizaje automático preentrenado.

Los argumentos **inputs** y **outputs** aceptan uno o más componentes de Gradio. Esta herramienta incluye más de 30 componentes integrados (como `gr.Textbox()`, `gr.Image()` y `gr.HTML()`) diseñados específicamente para aplicaciones de aprendizaje automático.

Si la función acepta más de un argumento, se debe pasar una lista de componentes a **inputs**, de modo que cada componente corresponda en orden a uno de los argumentos de la función. Lo mismo aplica si la función devuelve múltiples valores: se pasa una lista de componentes a **outputs**. Esta flexibilidad convierte a la clase `Interface` en una herramienta muy potente para crear demostraciones rápidas.

A continuación, se presenta la creación de una interfaz simple para un modelo de generación de descripciones de imágenes. Se utilizará el modelo BLIP (Preentrenamiento de Imágenes y Lenguaje por Bootstrap) para generar subtítulos descriptivos para las imágenes.

```bash
pip install transformers
pip install torch
```

```PYTHON
import gradio as gr
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Inicializar el procesador y el modelo desde Hugging Face
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image):
    # Se utiliza directamente el objeto de imagen PIL
    inputs = processor(images=image, return_tensors="pt")
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption

def caption_image(image):
    """
    Recibe una imagen PIL como entrada y devuelve una descripción.
    """
    try:
        caption = generate_caption(image)
        return caption
    except Exception as e:
        return f"Ocurrió un error: {str(e)}"

iface = gr.Interface(
    fn=caption_image,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Generación de Descripciones de Imágenes con BLIP",
    description="Sube una imagen para generar su descripción automática."
)
iface.launch(server_name="127.0.0.1", server_port= 7860)
```

En esta sección se emplean las clases `BlipProcessor` y `BlipForConditionalGeneration` de la biblioteca `transformers` para configurar un modelo de generación de descripciones para imágenes. Este ejemplo demuestra el proceso de creación de una interfaz web con Gradio, en la cual el parámetro de entrada es una imagen y la salida corresponde a la descripción en texto generada. Los parámetros de título y descripción mejoran la usabilidad al proporcionar contexto e instrucciones claras a los usuarios.

### Caso de uso: Generación de descripciones de imágenes

Los modelos de generación de descripciones de imágenes como BLIP son sumamente potentes en diversos ámbitos, desde brindar apoyo a personas con discapacidad visual para interpretar el contenido de una imagen, hasta la organización y búsqueda eficiente en grandes catálogos fotográficos. El desarrollo de una interfaz de Gradio para este tipo de modelos los hace accesibles para usuarios sin perfil técnico. Por ejemplo, los fotógrafos o gestores de activos digitales pueden emplear esta aplicación para catalogar automáticamente sus imágenes, mejorando la organización y capacidad de búsqueda de sus librerías digitales.

### Tarea 2: Clasificación de Imágenes en PyTorch

A continuación se presenta un tipo diferente de tarea de visión por computadora: la Clasificación de Imágenes. Esta es una de las tareas principales en la visión por computadora. El desarrollo de mejores clasificadores para identificar qué objeto se encuentra presente en una imagen constituye un área activa de investigación, ya que tiene aplicaciones que van desde vehículos autónomos hasta diagnóstico por imágenes médicas.

Estos modelos se integran de forma natural con el componente de entrada de imágenes de Gradio. En esta sección se detalla la creación de una demostración web para clasificar imágenes utilizando Gradio, implementando la totalidad de la aplicación en Python.

**Paso 1:** Configuración del modelo de clasificación de imágenes
En primer lugar, se requiere un modelo de clasificación de imágenes. En esta guía se utiliza un modelo Resnet-18 preentrenado, el cual puede descargarse fácilmente desde PyTorch Hub. No obstante, se puede utilizar un modelo preentrenado diferente o entrenar uno propio.

```PYTHON
import torch
model = torch.hub.load('pytorch/vision:v0.6.0', 'resnet18', pretrained=True).eval()
```

**Paso 2:** Definiendo una función de predicción
A continuación, se define una función encargada de recibir la entrada del usuario (una imagen) y retornar la predicción correspondiente en forma de diccionario, donde las claves son las etiquetas de clase y los valores representan las probabilidades de confianza calculadas. Las etiquetas legibles del modelo se cargan desde un enlace de texto de ImageNet.

```PYTHON
import torch
import requests
from torchvision import transforms

# Descargar las etiquetas legibles para ImageNet
response = requests.get("https://git.io/JJkYN")
labels = [l.strip() for l in response.text.split("\n") if l.strip()]

# Definir el preprocesamiento de la imagen (IMPORTANTE para ResNet)
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(
        [0.485, 0.456, 0.406],
        [0.229, 0.224, 0.225]
    )
])

def predict(inp):
    # Preprocesar la imagen
    inp = transform(inp).unsqueeze(0)
    # Asegurar que el modelo se ejecute en modo de inferencia
    with torch.no_grad():
        prediction = torch.nn.functional.softmax(model(inp)[0], dim=0)
    # Mapear las predicciones a sus respectivas etiquetas
    confidences = {
        labels[i]: float(prediction[i]) 
        for i in range(len(labels))
    }
    return confidences
```    

A continuación se analiza el funcionamiento del código. La función recibe un parámetro:

`inp: la imagen de entrada en formato PIL Image`

La función procesa la imagen de entrada y la convierte en un tensor de PyTorch. Tras evaluar el tensor a través del modelo, se retornan las predicciones en un diccionario denominado `confidences`. Las claves de este diccionario corresponden a las etiquetas de clase y los valores representan las probabilidades de confianza calculadas.

En esta sección se define una función de predicción encargada de procesar la imagen de entrada para estimar las probabilidades asociadas. La función convierte la imagen en un tensor de PyTorch y posteriormente la procesa a través del modelo preentrenado. Se aplica la función softmax en la etapa final para obtener la distribución de probabilidad de cada clase. La función softmax es fundamental porque transforma los logits crudos de salida del modelo (los cuales pueden ser cualquier número real) en probabilidades normalizadas cuya suma es igual a 1. Esto permite interpretar los resultados del modelo de forma directa como niveles de confianza para cada categoría.

**Paso 3:** Creación de una interfaz de Gradio
Una vez configurada la función de predicción, se procede a crear la interfaz de Gradio.

En este caso, el componente de entrada permite cargar imágenes mediante el método de arrastrar y soltar. Para instanciar esta entrada, se utiliza `gr.Image(type="pil")`, lo cual configura el componente y automatiza el preprocesamiento necesario para transformarlo en una imagen PIL.

El componente de salida es una etiqueta (`Label`), diseñada para mostrar las categorías más probables de forma estructurada. Dado que no se requiere visualizar las 1,000 clases posibles, se restringe la salida para mostrar únicamente las 3 principales utilizando `gr.Label(num_top_classes=3)`.

Finalmente, se implementa el parámetro `examples`, el cual permite precargar la interfaz con ejemplos de prueba específicos. El código de Gradio se detalla a continuación:

```PYTHON
import gradio as gr
gr.Interface(fn=predict,
       inputs=gr.Image(type="pil"),
       outputs=gr.Label(num_top_classes=3),
       examples=["/content/lion.jpg", "/content/cheetah.jpg"]).launch()
```

Las rutas de ejemplo proporcionadas (`/content/lion.jpg` y `/content/cheetah.jpg`) actúan como marcadores de posición. Se deben sustituir por las rutas reales de las imágenes en el sistema local o servidor de almacenamiento. Esto garantiza que, al ejecutar la interfaz de Gradio, los ejemplos se carguen correctamente para demostrar el funcionamiento del clasificador.

Esto produce una interfaz gráfica que se puede probar en cualquier navegador web.

Con estos pasos, se completa el desarrollo del código mínimo requerido para construir la demostración web de un clasificador de imágenes. En caso de requerir compartir la aplicación de forma pública, se puede configurar el argumento `share=True` al invocar el método `launch()` de la interfaz.
