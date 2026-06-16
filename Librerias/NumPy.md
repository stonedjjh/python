# Numpy

**NumPy** (abreviatura de _Numerical Python_) es la biblioteca fundamental para la computación científica en Python. Proporciona soporte para la creación y manipulación de arreglos y matrices multidimensionales de gran tamaño, junto con una amplia colección de funciones matemáticas de alto nivel para operar de manera eficiente sobre estas estructuras.

## Principales características de NumPy

1. **Objeto ndarray:** Su característica principal es el `ndarray` (arreglo n-dimensional), que es una estructura de datos rápida y flexible para conjuntos de datos grandes en Python.
2. **Eficiencia y velocidad:** A diferencia de las listas tradicionales de Python, los arreglos de NumPy están implementados en C y requieren que todos sus elementos sean del mismo tipo de dato. Esto permite realizar operaciones matemáticas complejas de manera mucho más rápida y consumiendo mucha menos memoria.
3. **Vectorización (Vectorization):** Permite realizar operaciones matemáticas a colecciones enteras de datos sin necesidad de iterar usando bucles `for`, lo que hace que el código sea más limpio, rápido y eficiente.
4. **Broadcasting:** Es un potente mecanismo que permite a NumPy trabajar con arreglos de diferentes formas y tamaños al realizar operaciones aritméticas.
5. **Ecosistema:** Es la base de casi todo el ecosistema de ciencia de datos en Python. Librerías como Pandas, SciPy, Matplotlib, y Scikit-learn están construidas directamente sobre NumPy.

## Instalación de NumPy

Para instalar NumPy, puedes usar el siguiente comando en tu terminal o línea de comandos:

```bash
pip install numpy
```

## Ejemplos de uso de NumPy

A continuación, se presentan algunos ejemplos básicos para empezar a trabajar con NumPy.

### 1. Importación y creación de arreglos

```python
import numpy as np

# Crear un arreglo (array) unidimensional a partir de una lista
arr1 = np.array([1, 2, 3, 4, 5])
print("Array 1D:", arr1)

# Crear un arreglo bidimensional (matriz) a partir de listas anidadas
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("Array 2D:\n", arr2)

# Arreglos especiales precargados
ceros = np.zeros((3, 3))        # Matriz 3x3 llena de ceros
unos = np.ones((2, 4))          # Matriz 2x4 llena de unos
aleatorios = np.random.rand(2)  # Array de 2 números aleatorios entre 0 y 1

# Arreglo con una secuencia de números
secuencia = np.arange(0, 10, 2) # Del 0 al 10 (exclusivo) con saltos de 2
print("Secuencia:", secuencia)  # Salida: [0 2 4 6 8]
```

### 2. Atributos de un arreglo

Los objetos `ndarray` tienen atributos útiles para conocer cómo están estructurados.

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print("Número de dimensiones (ndim):", arr.ndim)       # Salida: 2
print("Forma del arreglo (shape):", arr.shape)         # Salida: (2, 3) - 2 filas, 3 columnas
print("Tamaño total (size):", arr.size)                # Salida: 6 elementos
print("Tipo de dato (dtype):", arr.dtype)              # Ej: int32 o int64
```

### 3. Operaciones matemáticas (Vectorización)

Las operaciones matemáticas en NumPy se aplican elemento por elemento de forma nativa.

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

# Operaciones elemento por elemento
print("Suma:", a + b)           # [11 22 33]
print("Resta:", b - a)          # [ 9 18 27]
print("Multiplicación:", a * b) # [10 40 90]
print("División:", b / a)       # [10. 10. 10.]

# Multiplicación por un escalar
print("Escalar:", a * 5)        # [ 5 10 15]
```

### 4. Indexación y Segmentación (Slicing)

Funciona de manera muy similar a las listas estándar de Python, pero extendida a múltiples dimensiones.

```python
arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

# Acceder a un elemento específico (Fila 0, Columna 1)
print("Elemento en 0,1:", arr[0, 1])  # Salida: 20

# Obtener toda una fila entera
print("Primera fila:", arr[0, :])     # Salida: [10 20 30]

# Obtener toda una columna entera
print("Segunda columna:", arr[:, 1])  # Salida: [20 50 80]

# Indexación usando una lista de posiciones
c = np.array([100, 1, 2, 3, 4])
select = [0, 2, 3, 4]           # Índices que queremos seleccionar
print("Índices seleccionados:", select)

d = c[select]                    # Extrae los elementos en las posiciones 0, 2, 3 y 4
print("Resultado:", d)          # Salida: [100   2   3   4]
```

### 5. Generación de datos continuos (Linspace)

Una función sumamente útil para graficar funciones matemáticas o simular señales continuas es `np.linspace`. A diferencia de `np.arange` (que requiere un tamaño de paso), `linspace` te permite especificar cuántos elementos exactos deseas obtener distribuidos uniformemente dentro de un rango cerrado.

**Sintaxis básica:**
`numpy.linspace(start, stop, num)`

- **start:** El valor inicial del intervalo.
- **stop:** El valor final del intervalo (por defecto, este límite es **inclusivo**).
- **num:** El número de muestras o elementos que deseas generar de forma equidistante.

```python
# Generar 5 números distribuidos uniformemente entre 0 y 100
linea = np.linspace(0, 100, num=5)
print("Intervalo uniforme (5 elementos):", linea)
# Salida: [  0.  25.  50.  75. 100.]

# Muy útil en cálculo y gráficos para evaluar funciones (ej. generar 100 puntos entre 0 y 2*PI)
puntos_pi = np.linspace(0, 2 * np.pi, num=100)
print("Primeros 3 puntos de PI:", puntos_pi[:3])
```

### 6. Funciones Estadísticas y Matemáticas

NumPy incluye una extensa cantidad de funciones estadísticas integradas y listas para usar:

```python
datos = np.array([15, 20, 35, 40, 50])

print("Media:", np.mean(datos))
print("Mediana:", np.median(datos))
print("Desviación estándar:", np.std(datos))
print("Valor máximo:", np.max(datos))
print("Valor mínimo:", np.min(datos))
```

## Operaciones con NumPy

Esta es la lista de operaciones que se pueden realizar con NumPy:

| Operación                         | Descripción                                   | Ejemplo                                            |
| :-------------------------------- | :-------------------------------------------- | :------------------------------------------------- |
| **Creación de Array**             | Creación de un array NumPy.                   | `arr = np.array([1, 2, 3, 4, 5])`                  |
| **Aritmética por elementos**      | Suma, resta, etc. de elementos.               | `result = arr1 + arr2`                             |
| **Aritmética Escalar**            | Suma, resta, etc. de escalares.               | `result = arr * 2`                                 |
| **Funciones a nivel de elemento** | Aplicación de funciones a cada elemento.      | `result = np.sqrt(arr)`                            |
| **Suma y media**                  | Cálculo de la suma y la media de una matriz.  | `total = np.sum(arr)`<br>`average = np.mean(arr)`  |
| **Valores máximos y mínimos**     | Encontrar los valores máximos y mínimos.      | `max_val = np.max(arr)`<br>`min_val = np.min(arr)` |
| **Reformar**                      | Modificación de la forma de una matriz.       | `reshaped_arr = arr.reshape(2, 3)`                 |
| **Transposición**                 | Transposición de una matriz multidimensional. | `transposed_arr = arr.T`                           |
| **Multiplicación de matrices**    | Multiplicación de matrices.                   | `result = np.dot(matrix1, matrix2)`                |

## Conclusión

NumPy es esencial para cualquier proyecto que involucre manipulación intensiva de datos, simulaciones científicas o cálculos matemáticos en Python. Su capacidad de manejar grandes volúmenes de datos mediante operaciones vectorizadas lo convierte en una herramienta indispensable, complementando perfectamente a otras librerías orientadas a datos como Pandas.
