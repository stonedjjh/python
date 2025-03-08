#python no usas {} para definir bloques de codigo, sino que usa identacion. 
def suma(a, b): # Definimos la función "suma". Tiene 2 parámetros.
    return a+b # "return" devuelve el resultado de la función.

print(suma(2, 3)) # Llamada a la función. Hay que pasarle dos parámetros.
# Resultado: 5

def en_pantalla(frase1, frase2):
    print(frase1, frase2) # "return" no es obligatorio
en_pantalla('Me gusta', 'Python')


print("")#imprimer una linea vacia
print('funciones anidadas')
#funciones anidadas
def f1(a): # Función que "encierra"    a f2 (enclosing)
    print(a)
    b = 100
    def f2(x): # Función anidada
        print(x) # Llamamos a f2 desde  f1
    f2(b)
f1('Python') # Llamamos a f1


print("")
print('recursividad')
#recursividad
def factorial(x):
    if x>1:
        return x*factorial(x-1)
    else:
        return 1
print('El factorail de 5 es:',factorial(5))


print("")
print('Devolviendo multiples valores')
#Devolviendo multiples valores
def maxmin(lista):
    return max(lista), min(lista) #Devielveuna tupla de 2 elementos

l = [1, 3, 5, 6, 0]
maximo, minimo = maxmin(l) #Desempaqueta la tupla en 2 variables
print('el minimo es: ',minimo,'el maximo es: ',maximo, sep= ' ')

#ambito de variables en funciones
print("")#imprimer una linea vacia
print('ambito de variables en funciones')
G = 'Esta variable es de ámbito Global'
def f1():
    E='Esta variable es local a f1. Enclosing a f2'
    def f2():
        L = 'Esta variable es local a f2'
        print(L, E, G, sep = '\n')
    f2()
f1()

#ejemplo con argumentos inmutable
def suma(a, b): # Modificamos a y b en el scope de suma()
    a = 3
    b = 4
    return a+b
a, b = 5, 10
print(suma(a, b))
print(a, b) # a y b no han cambiado fuera de la función

#ejemplo con argumentos mutables
def modificar_lista(lista):
    lista.append(4)  # Modifica la lista original
    lista[0] = 10  # Modifica la lista original

mi_lista = [1, 2, 3]
print(mi_lista)  # Imprime: [1, 2, 3]
modificar_lista(mi_lista)
print(mi_lista)  # Imprime: [10, 2, 3, 4]

#un vistazo a como podemos pasar argumentos
print("")
print('Pase de argumentos')

#por posicion
def f(a, b, c):
    print('por posicion f(1,2,3) ',a, b, c)
f(1,2,3)    

#por keyword
def f(a, b, c):
    print('por keyword f(c=12, a=10, b=100) ',a, b, c)
f(c=12, a=10, b=100)

#con valores por defecto 
def f(a, b=10, c=30):
    return (a, b, c)

print('con valores por defecto (a, b=10, c=30) f(1)',f(1))
print('con valores por defecto (a, b=10, c=30) f(1, 12)', f(1,12))
print('con valores por defecto (a, b=10, c=30) f(1,12,19)', f(1, 12, 19))

#con n cantidad de argumentos 

def f(*args): # Acepta número arbitrario de argumentos
    return (args)

print("")
print("f(*args)")
print('con f()',f())
print('con f(1)',f(1))
print('con f(1, 2)',f(1, 2))
print('con f(1, 2, 3, 4, 5, 6)',f(1, 2, 3, 4, 5, 6))

#con n cantidad de argumentos por nombre
def f(**Kargs): # Acepta número de argumentos por nombre
    return (Kargs)

print("")
print("f(**Kargs)")
print('con f()',f())# Si no hay argumentos, Karg
print('con f(a=1)',f(a=1))
print('con f(a=1, b=2)',f(a=1, b=2))
print('con f(a=1, c=3, b=2)',f(a=1, c=3, b=2))

#Desempaquetado
def f(a, b , c ,d): 
    return (a,b,c,d)


print('Desempaquetado con f(*[1,2,3,4])',f(*[1,2,3,4])) 
print('Desempaquetado con f(100, *[1,2,3])',f(100, *[1,2,3]))
print('Desempaquetado con f(100,200,*[1,2])',f(100,200,*[1,2]))

def f(a, b , c ,d): 
    print (a,b,c,d)

f(*[1,2,3,4])
f(100, *[1,2,3])
f(*[100,200],*[1,2])

#Desempaquetado con **
def f(a, b, c, d):
    return (a, b, c, d)

# Desempaquetando diccionario argumentos con **
print("Desempaquetado con f(**{'b':20, 'a':1, 'c':300,'d':4000}))",f(**{'b':20, 'a':1, 'c':300,'d':4000})) 
argumentos = {'b':200, 'c':300, 'd':400}
# Podemos combinar argumentos posicionales con dict
print("Desempaquetado con f(10,{'b':200, 'c':300, 'd':400} ))",f(10,**{'b':200, 'c':300, 'd':400})) 

#Utilizando argumentos que sólo pueden ser pasados por clave 

def f(a, *, b, c): # Define 'b' y 'c' como keyword-only con el *
    print(a, b, c)
f(1, b=10, c=100)
#f(1, 10, 100) # Error al no pasar argumentos Keyword-only

def f(a, *b, c): # Hay que pasar 'c' por clave obligatoriamente
    print(a, b, c)
f(1, c=2)
f(1, 2, c=3)
f(1, 2, 3, 4, 5, c=10)