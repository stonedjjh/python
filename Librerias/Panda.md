# Panda

Pandas es una popular librería de análisis y manipulación de datos de código abierto para el lenguaje de programación Python. Proporciona un conjunto potente y flexible de herramientas para trabajar con datos estructurados, por lo que es una herramienta fundamental para los científicos de datos, analistas e ingenieros.Pandas está diseñado para manejar datos en varios formatos, tales como datos tabulares, datos de series temporales, y más, por lo que es una parte esencial del flujo de trabajo de procesamiento de datos en muchas industrias.

## Principales características y funcionalidades de Pandas

**Estructuras de datos:** Pandas ofrece dos estructuras de datos principales: DataFrame y Series.

1. Un DataFrame es una estructura de datos tabular bidimensional, de tamaño modificable y potencialmente heterogénea con ejes etiquetados (filas y columnas).

2. Una serie es una matriz unidimensional etiquetada, esencialmente una sola columna o fila de datos.

**Importación y exportación de datos:** Pandas facilita la lectura de datos de varias fuentes, incluyendo archivos CSV, hojas de cálculo Excel, bases de datos SQL y más. También puede exportar datos a estos formatos, lo que permite un intercambio de datos sin problemas.

**Fusión y unión de datos:** Puede combinar múltiples DataFrames utilizando métodos como fusionar y unir, similares a las operaciones SQL, para crear conjuntos de datos más complejos a partir de diferentes fuentes.

**Indexación eficiente:** Pandas proporciona métodos eficientes de indexación y selección, permitiéndole acceder rápidamente a filas y columnas específicas de datos.

**Estructuras de datos personalizadas:** Puede crear estructuras de datos personalizadas y manipular los datos de forma que se adapten a sus necesidades específicas, ampliando las capacidades de Pandas.

## Instalación de Pandas

Para instalar Pandas, puede usar el siguiente comando en su terminal o línea de comandos:

```bash
pip install pandas
```

## Ejemplo de uso de Pandas

Aquí hay un ejemplo básico de cómo usar Pandas para crear un DataFrame, realizar algunas operaciones básicas y mostrar los resultados:

```python
import pandas as pd
# Crear un DataFrame a partir de un diccionario
data = {
    'Nombre': ['Alice', 'Bob', 'Charlie'],
    'Edad': [25, 30, 35],
    'Ciudad': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
# Mostrar el DataFrame
print(df)
# Acceder a una columna específica
print(df['Nombre'])
# Filtrar filas basadas en una condición
mayores_30 = df[df['Edad'] > 30]
print(mayores_30)
# Agregar una nueva columna
df['Salario'] = [50000, 60000, 70000]
print(df)
```

En este ejemplo, creamos un DataFrame con información sobre personas, accedemos a una columna específica, filtramos filas basadas en una condición y agregamos una nueva columna al DataFrame. Pandas ofrece muchas más funcionalidades para manipular y analizar datos de manera eficiente.

## Carga de datos

Pandas se puede utilizar para cargar datos de varias fuentes, como archivos CSV y Excel.

La función read_csv se utiliza para cargar datos de un archivo CSV en un DataFrame de Pandas.

Para leer un fichero CSV (Comma-Separated Values) en Python usando la librería Pandas, puedes usar la función pd.read_csv(). Aquí está la sintaxis para leer un archivo CSV:

```PYTHON
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('your_file.csv')
```

Donde

- `pd` es el alias comúnmente utilizado para importar la librería Pandas.

- `'your_file.csv'` es la ruta al archivo CSV que deseas leer. Puede ser una ruta relativa o absoluta.

- `df` es un objeto DataFrame de Pandas que contiene los datos del archivo CSV.

## ¿Qué es una serie?

Una Serie es un array unidimensional etiquetado en Pandas. Puede considerarse como una única columna de datos con etiquetas o índices para cada elemento. Se pueden crear series a partir de varias fuentes de datos, como listas, arrays NumPy o diccionarios:

```PYTHON
import pandas as pd
# Create a Series from a list
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)
```

### Acceso a los elementos de una serie

Puede acceder a los elementos de una Serie utilizando las etiquetas de índice o las posiciones de los enteros. Estos son algunos métodos comunes para acceder a los datos de las series:

**Acceso por etiqueta:**

`print(s[2])     # Access the element with label 2 (value 30)`

**Acceso por posición:**

`print(s.iloc[3]) # Access the element at position 3 (value 40)`

**Acceso a un rango de elementos:**

`print(s[1:4])   # Access elements from position 1 to 3 (values 20, 30, 40)`

## Atributos y métodos de las series

Las Series de Pandas vienen con varios atributos y métodos que le ayudarán a manipular y analizar los datos de forma efectiva. Aquí tienes algunos esenciales:

- **valores**: Devuelve los datos de la Serie como un array NumPy.

- **índice**: Devuelve el índice (etiquetas) de la Serie.

- **shape**: Devuelve una tupla que representa las dimensiones de la Serie.

- **tamaño**: Devuelve el número de elementos de la Serie.

- **media(), suma(), min(), max()**: Calcula estadísticas de resumen de los datos.

- **unique(), nunique()**: Obtener valores únicos o el número de valores únicos.

- **sort_values(), sort_index()**: Ordena las series por valores o etiquetas de índice.

- **isnull(), notnull()**: Comprueba si faltan valores (NaN) o no faltan valores.

- **apply()**: Aplica una función personalizada a cada elemento de la Serie.

## ¿Qué es un DataFrame?

Un DataFrame es una estructura de datos bidimensional etiquetada con columnas de tipos de datos potencialmente diferentes. Piense en ello como una tabla donde cada columna representa una variable, y cada fila representa una observación o punto de datos. Los DataFrames son adecuados para una amplia gama de datos, incluidos los datos estructurados de archivos CSV, hojas de cálculo Excel, bases de datos SQL, etc.

### Creación de DataFrames a partir de diccionarios

Los DataFrames pueden crearse a partir de diccionarios, con claves como etiquetas de columna y valores como listas que representan filas.

```PYTHON
import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

print(df)
```

**Selección de columnas:**

Puede seleccionar una sola columna de un DataFrame especificando el nombre de la columna entre corchetes dobles.

`print(df['Name'])  # Access the 'Name' column`

**Acceso a las filas:**

Puede acceder a las filas por su índice utilizando .iloc[] o por etiqueta utilizando .loc[].

```PYTHON
print(df.iloc[2])   # Access the third row by position
print(df.loc[1])    # Access the second row by label
```

**Rebanar:**

Puede cortar los DataFrames para seleccionar filas y columnas específicas.

```PYTHON
print(df[['Name', 'Age']])  # Select specific columns
print(df[1:3])             # Select specific rows
```

### Búsqueda de elementos únicos

Utilice el método unique para determinar los elementos únicos de una columna de un DataFrame.

`unique_dates = df['Age'].unique()`

### Filtrado condicional

Puede filtrar los datos de un DataFrame basándose en condiciones mediante operadores de desigualdad.

`high_above_102 = df[df['Age'] > 25]`

### Guardar marcos de datos

Para guardar un DataFrame en un archivo CSV, utilice el método to_csv y especifique el nombre del archivo con una extensión ".csv".Pandas proporciona otras funciones para guardar DataFrames en diferentes formatos.

`df.to_csv('trading_data.csv', index=False)`

### Atributos y métodos de DataFrame

Los DataFrames proporcionan numerosos atributos y métodos para la manipulación y el análisis de datos, incluyendo:

- **forma:** Devuelve las dimensiones (número de filas y columnas) del DataFrame.

- **info():** Proporciona un resumen del DataFrame, incluyendo los tipos de datos y los recuentos no nulos.

- **describe():** Genera estadísticas de resumen para columnas numéricas.

- **head(), tail():** Muestra las n primeras o últimas filas del DataFrame.

- **mean(), sum(), min(), max():** Calcula las estadísticas de resumen de las columnas.

- **ordenar_valores():** Ordena el DataFrame por una o más columnas.

- **groupby():** Agrupa los datos basándose en columnas específicas para la agregación.

- **fillna(), drop(), rename():** Manejar valores perdidos, eliminar columnas o renombrar columnas.

- **apply():** Aplica una función a cada elemento, fila o columna del DataFrame.

Pandas ofrece una amplia gama de métodos más allá de estos ejemplos. Para obtener información más detallada, consulte la documentación oficial disponible en el
[sitio web oficial de Pandas](https://pandas.pydata.org/docs/).

## Conclusión

En conclusión, dominar el uso de Pandas Series y DataFrames es esencial para una manipulación y análisis de datos eficaz en Python. Las Series proporcionan una base para manejar datos unidimensionales con etiquetas, mientras que los DataFrames ofrecen una estructura versátil, similar a una tabla, para trabajar con datos bidimensionales. Tanto si está limpiando, explorando, transformando o analizando datos, estas estructuras de datos de Pandas, junto con sus atributos y métodos, le permiten manipular los datos de forma eficiente y flexible para obtener información valiosa. Al incorporar Series y DataFrames a su conjunto de herramientas de ciencia de datos, estará bien preparado para abordar una amplia gama de tareas relacionadas con los datos y mejorar sus capacidades de análisis de datos:

- Trabaja con conjuntos de datos reales para aplicar lo que has aprendido y adquirir experiencia práctica.

- Visite el[sitio web oficial de Pandas](https://pandas.pydata.org/docs/) para explorar la extensa documentación y descubrir más funciones y métodos.

## Ejercicios

```PYTHON
import pandas as pd
#Define a dictionary 'x'

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'],
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
df
# SALIDA
#	Name	ID	Department	Salary
#0	Rose	1	Architect Group	100000
#1	John	2	Software Group	80000
#2	Jane	3	Design Team	50000
#3	Mary	4	Infrastructure	60000
x = df[['ID']]
x

# 	ID
# 0	1
# 1	2
# 2	3
# 3	4

type(x)
pandas.DataFrame

z = df[['Department','Salary','ID']]
z

#   Department	Salary	ID
# 0	Architect Group	100000	1
# 1	Software Group	80000	2
# 2	Design Team	50000	3
# 3	Infrastructure	60000	4


```

Try it yourself

Problem 1: Create a dataframe to display the result as below:

```PYTHON
students = {'Student':['David','Samuel','Terry','Evan'],'Age':[27,24,22,32],'Country':['UK','Canada','China','USA'],'Course':['Python','Data Structures','Machine Learning','Web Development']
,'Marks':[85,72,89,76]}
df = pd.DataFrame(students)
df

#   Student	Age	Country	Course	Marks
# 0	David	27	UK	Python	85
# 1	Samuel	24	Canada	Data Structures	72
# 2	Terry	22	China	Machine Learning	89
# 3	Evan	32	USA	Web Development	76

# Problem 2: Retrieve the Marks column and assign it to a variable b

b = df[['Marks']]
b

# 	 Marks
# 0	 85
# 1	 72
# 2	 89
# 3	 76

# Problem 3: Retrieve the Country and Course columns and assign it to a variable c

c = df[['Country','Course']]

#   Country	Course
# 0	UK	    Python
# 1	Canada	Data Structures
# 2	China	Machine Learning
# 3	USA	    Web Development

# To view the column as a series, just use one bracket:

x = df['Student']
x

# 0     David
# 1    Samuel
# 2     Terry
# 3      Evan
# Name: Student, dtype: str
type(x)
pandas.Series


df.iloc[0, 0]
# 'Rose'

df.iloc[0,2]
# 'Architect Group'

df.loc[0, 'Name']
# 'Rose'

df.loc[0, 'Salary']
np.int64(100000)

# Let us create a new dataframe called 'df2' and assign 'df' to it. Now, let us set the "Name" column as an index column using the method set_index().

df2=df
df2=df2.set_index("Name")

df2.head()

#        ID	Department	Salary
# Name
# Rose	1	Architect Group	100000
# John	2	Software Group	80000
# Jane	3	Design Team	50000
# Mary	4	Infrastructure	60000

#Now, let us access the column using the name
df2.loc['Jane', 'Salary']
# np.int64(50000)

# Use the loc() function,to get the Department of Jane in the newly created dataframe df2.
df2.loc['Jane', 'Department']
# 'Design Team'

# Use the iloc() function to get the Salary of Mary in the newly created dataframe df2.
df2.iloc[3, 2]
# np.int64(60000)

#Exercise 3: Slicing

# let us do the slicing using old dataframe df

df.iloc[0:2, 0:3]
# 	Name	ID	Department
# 0	Rose	1	Architect Group
# 1	John	2	Software Group

#let us do the slicing using loc() function on old dataframe df where index column is having labels as 0,1,2
df.loc[0:2,'ID':'Department']

# 	ID	Department
# 0	1	Architect Group
# 1	2	Software Group
# 2	3	Design Team

#let us do the slicing using loc() function on new dataframe df2 where index column is Name having labels: Rose, John and Jane
df2.loc['Rose':'Jane', 'ID':'Department']

#         ID	Department
# Name
# Rose	1	Architect Group
# John	2	Software Group
# Jane	3	Design Team

# Write your code below and press Shift+Enter to execute
df.loc[ 2:3 ,'Name':'Department']

# 	Name	ID	Department
# 2	Jane	3	Design Team
# 3	Mary	4	Infrastructure

```

### Lectura de Archivos con Panda

```PYTHON
from pyodide.http import pyfetch
import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())


await download(filename, "Product-sales.csv")
df = pd.read_csv("Product-sales.csv")

# Print first five rows of the dataframe

df.head()

# OrderID   Product     Category    Quantity    Price   Total   OrderDate       CustomerCity
# 0     1    Laptop     Electronics   2         800       1600    2022-01-10    New York
# 1     2    Smartphone Electronics   3         600       1800    2022-02-15    Los Angeles
# 2     3    Desk Chair Furniture     5         150        750    2022-03-12    Chicago
# 3     4    Notebook   Stationery   10         2           20    2022-04-05    Houston
# 4     5    Monitor    Electronics   1         300         300   2022-05-21    Miami


# Read data from Excel File and print the first five rows

xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n9LOuKI9SlUa1b5zkaCMeg/Product-sales.xlsx'

await download(xlsx_path, "Product-sales.xlsx")
df = pd.read_excel("Product-sales.xlsx")
df.head()

# OrderID   Product     Category    Quantity    Price   Total   OrderDate       CustomerCity
# 0     1    Laptop     Electronics   2         800       1600    2022-01-10    New York
# 1     2    Smartphone Electronics   3         600       1800    2022-02-15    Los Angeles
# 2     3    Desk Chair Furniture     5         150        750    2022-03-12    Chicago
# 3     4    Notebook   Stationery   10         2           20    2022-04-05    Houston
# 4     5    Monitor    Electronics   1         300         300   2022-05-21    Miami

# Access to the column Length

x = df[['Quantity']]
x

# 	    Quantity
# 0 	2
# 1 	3
# 2 	5
# 3 	10
# 4 	1

# Get the column as a series

x = df['Product']
x

# 0        Laptop
# 1    Smartphone
# 2    Desk Chair
# 3      Notebook
# 4       Monitor
# Name: Product, dtype: object

# Get the column as a dataframe

x = df[['Quantity']]
type(x)

pandas.core.frame.DataFrame

# Access to multiple columns

y = df[['Product','Category', 'Quantity']]
y


```
