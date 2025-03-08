#una lista es una estructura de datos versátil, heterogenea, indexada y mutable que se utiliza para almacenar 
# una colección ordenada de elementos, que se pueden repetir. 
#definimos una lista 
frutas = ["Manazana", "Pera", "Uva", "Melón"]
#la imprimimos
print("las frutas en la lista son: ", frutas)

#para obtener un sublitas podemos especificar el rango
#el primer valor del rango dato es inclusivo y el segundo es exclusivo
print("para obtener una parte de la lista podemos usar frutas[1:3]", frutas[1:3])

#para obtener un sublitas podemos especificar el rango con valores negativos para obtener los elementos
#desde el final de la lista
#el primer valor del rango dato es inclusivo y el segundo es exclusivo
print("podemos usar rangos negativos y tomamos del final frutas[-4:-1]",frutas[-4:-1])

#para agregar un elemento a la lista usamos el metodo append
frutas.append("Mango")
print("para agregar elementos podemos usar el metodo append frutas.append(\"Mango\") ",frutas)

#para recorrer la lista podemos usar un bucle for
print("para recorrer la lista podemos usar un bucle for in")
for fruta in frutas:
    print(fruta)

#la palabra reservada in tambien nos permite saber si un elemento esta en la lista
print("la palabra reservada in tambien nos permite saber si un elemento esta en la lista \"Uva\" in frutas", "Uva" in frutas)   

#para obtener la longitud de la lista usamos la funcion len
print("la longitud de la lista",frutas,"es:", len(frutas))

#para cambiar el valor de un elemento podemos referrenciarlo por su indice
frutas[0] = "Fresa"
print("para cambiar el valor de un elemento podemos referrenciarlo por su indice frutas[0] = \"Fresa\"",frutas)

#copia de una lista
#frutas2= frutas solo apuntaria a la misma direccion de memoria por lo cual los cambios en una lista
#se verian reflejados en la otra
frutas2= frutas
print("frutas2= frutas ,frutas apunta a" , id(frutas), "fruta2 apunta a" , id(frutas2))

print("para copiar una lista no se puede asignar a otra variable, se debe usar el metodo copy")

frutas2= frutas.copy()
print("frutas2= frutas.copy() ,frutas apunta a" , id(frutas), "fruta2 apunta a" , id(frutas2))

#otra forma de copiar una lista es usar el consttructor list
frutas3 = list(frutas)

print("frutas3 = list(frutas) ,frutas apunta a" , id(frutas), "fruta2 apunta a" , id(frutas3))

#unir listas 
frutas4 = ["Sandia", "Papaya", "Melón"]

#lo podemos unir con el operador + 
frutas5= frutas + frutas4
print("Creamos otra lista frutas4 = [\"Sandia\", \"Papaya\", \"Melón\"]")
print("lo podemos unir con el operador + frutas5= frutas + frutas4",frutas5)

#podemos limpiar una lista con el metodo clear
frutas5.clear()
print("Podemos borrar una lista con el metodo clear frutas5.clear()",frutas5)
print("frutas5", frutas5)

#tambien podemos recorre la lista y agregar los elementos
frutas5.clear()
for fruta in frutas:
    frutas5.append(fruta)

for fruta in frutas4:
    frutas5.append(fruta)

print("lo podemos unir con append dentro de un for",frutas5)    

#O con el metodo extend

frutas5.clear()
frutas5.extend(frutas)
frutas5.extend(frutas4)
print("lo podemos unir con el metodo extend frutas5.extend(frutas) frutas5.extend(frutas4)",frutas5)

#podemos saber cuantas veces se repite un elemento en la lista con el metodo count

print("Melón se encuentra ",frutas5.count("Melón"), "veces en la lista" if frutas5.count("Melón") > 1 else "veces en la lista")
print("Kiwi se encuentra ", frutas5.count("Kiwi"), "veces en la lista" if frutas5.count("Kiwi") > 1 else "vez en la lista")

#con la palabra reservada del podemos eliminar un elemento de la lista por su indice o toda la lista
del frutas5[0]
print("del frutas5[0]", frutas5)
del frutas5
#print("del frutas5", frutas5) esto daria un error ya que frutas5 no existe


#tupla
#una tupla es una estructura de datos inmutable, heterogenea, indexada y ordenada 
# que se utiliza para almacenar una colección ordenada de elementos, que se pueden repetir.
#una tupla es una secuencia ordenada e inmutable de elementos. 

#definimos una tupla
paises = ("Mexico", "Argentina", "Colombia", "Chile","Mexixo")#una tupla se define con parentesis

print("La tupla paises contiene:" , paises)

#Crear tupla con un artículo

x = ("Mexico",)
print("para crear una tupla de un solo valor lo hacemos asi (\"Mexico\",)",type(x))
x = ("Mexico")
print("de esta forma no sera una tupla (\"Mexico\")",type(x))

#Diccionarios es un estructura de datos no ordenada, mutable e indexada, que se componen de pares 
#clave, valor,  Las claves en un diccionario deben ser únicas.

persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}#usamos llaves para declarar un diccionario
#comas para separar elementos y : para dividir la clave y el valor
print("El diccionario persona se ve asi: ",persona)

#otra forma de declarar un diccionario es con la funcion dict
dic2 = dict(
Nombre="Santiago",
Apellido="Hernandez",
Pais="España",
Ciudad="Madrid"
)

print("El diccionario dic2 se ve asi: ",dic2)

#para obtener las claves usamos la palabra reservada keys
claves = persona.keys()
print ("Con persona.keys() obentemos las claves:", claves)
#para obtener los valores usamos la palabra reservada values
valores = persona.values()
print ("Con persona.values() obentemos los valores:", valores)

#para limpiar un diccionario usamos el metodo clear
dic2.clear()
print("Despues de usar dic2.clear():", dic2)

#para copiar un diccionario usamos el metodo copy
persona_copia = persona.copy()
print("Para copiar un dicionario usamos persona_copia = persona.copy():", persona_copia)
print("persona apunta a", id(persona), "persona_copia apunta a", id(persona_copia))

#para crear un diccionario con claves especificas y un valor predeterminado usamos fromkeys
claves = ("nombre", "edad", "ciudad")
valores = "desconocido"
nuevo_dic = dict.fromkeys(claves, valores)
print("Diccionario creado con fromkeys:", nuevo_dic)

#para obtener el valor de una clave especifica usamos get
edad = persona.get("edad")
print("con persona.get(\"edad\") obtnemos la edad del diccionario persona:", edad)

#para obtener los pares clave-valor usamos items
items = persona.items()
print(" items = persona.items() Los pares clave-valor del diccionario persona son:", items)

#para obtener las claves usamos keys
claves = persona.keys()
print("Las claves del diccionario persona son:", claves)

#para eliminar un elemento especifico usamos pop
ciudad = persona.pop("ciudad")
print("Despues de usar persona.pop('ciudad'):", persona)
#recordemos que pop devuelve el valor eliminado
print("ciudad:", ciudad)

#para eliminar el ultimo par clave-valor usamos popitem
ultimo_item = persona.popitem()
print("Despues de usar persona.popitem():", persona)
print("popitem:", ultimo_item)

#para establecer un valor predeterminado si la clave no existe usamos setdefault
pais = persona.setdefault("pais", "España")
print("Despues de usar setdefault('pais', 'España'):", persona)

#para actualizar un diccionario con otro diccionario usamos update
persona.update({"nombre": "Carlos", "edad": 35})
print("Despues de usar update({'nombre': 'Carlos', 'edad': 35}):", persona)

#para obtener los valores usamos values
valores = persona.values()
print("Los valores del diccionario persona son:", valores)

#sets o conjuntos
#un conjunto es una colección no ordenada y no indexada de elementos únicos, heterogeneos.
#se definen con llaves
# Definimos un set
frutas_set = {"Manzana", "Pera", "Uva",5, 4, 5}

print("El set frutas_set es:", frutas_set)

# add() Añade un elemento al set
frutas_set.add("Melón")
print("Después de frutas_set.add(\"Melón\"):", frutas_set)

# clear() Borra todos los elementos del set
frutas_set.clear()
print("Después de clear():", frutas_set)

# copy() Devuelve una copia del set
frutas_set = {"Manzana", "Pera", "Uva"}
frutas_set_copia = frutas_set.copy()
print("Después de copy():", frutas_set_copia)

# difference() Devuelve un set que contiene las diferencias entre dos o más sets
frutas_set2 = {"Pera", "Melón"}
diferencia = frutas_set.difference(frutas_set2)
print("Después de difference(frutas_set2):", diferencia)

# difference_update() Borra los elementos del set que están incluidos en otro
frutas_set.difference_update(frutas_set2)
print("Después de difference_update(frutas_set2):", frutas_set)

# discard() Borra el elemento especificado
frutas_set.discard("Pera")
print("Después de discard('Pera'):", frutas_set)

# intersection() Devuelve un set que es la intersección resultante de otros dos
frutas_set = {"Manzana", "Pera", "Uva"}
interseccion = frutas_set.intersection(frutas_set2)
print("Después de intersection(frutas_set2):", interseccion)

# intersection_update() Borra los elementos del set que no están presentes en otro
frutas_set.intersection_update(frutas_set2)
print("Después de intersection_update(frutas_set2):", frutas_set)

# isdisjoint() Informa si dos sets tienen una intersección o no
frutas_set = {"Manzana", "Pera", "Uva"}
disjoint = frutas_set.isdisjoint(frutas_set2)
print("Después de isdisjoint(frutas_set2):", disjoint)

# issubset() Informa si otro set contiene a este set o no
subset = frutas_set.issubset(frutas_set2)
print("Después de issubset(frutas_set2):", subset)

# issuperset() Informa si este set contiene a otro set o no
superset = frutas_set.issuperset(frutas_set2)
print("Después de issuperset(frutas_set2):", superset)

# pop() Borra un elemento del set, no podremos elegir cuál.
elemento = frutas_set.pop()
print("Después de pop():", frutas_set, "Elemento eliminado:", elemento)

# remove() Borra un elemento específico
frutas_set.remove("Pera")
print("Después de remove('Pera'):", frutas_set)

# symmetric_difference() Devuelve un set con las diferencias simétricas de dos sets
frutas_set = {"Manzana", "Pera", "Uva"}
simetrica = frutas_set.symmetric_difference(frutas_set2)
print("Después de symmetric_difference(frutas_set2):", simetrica)

# symmetric_difference_update() Inserta las diferencias simétricas de este set y otro
frutas_set.symmetric_difference_update(frutas_set2)
print("Después de symmetric_difference_update(frutas_set2):", frutas_set)

# union() Devuelve un set con la unión de dos sets
union = frutas_set.union(frutas_set2)
print("Después de union(frutas_set2):", union)

# update() Actualiza el set con la unión de este set y otros
frutas_set.update(frutas_set2)
print("Después de update(frutas_set2):", frutas_set)
