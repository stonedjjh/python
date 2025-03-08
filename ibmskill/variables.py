#Python es un lenguaje de tipado debil
s_nombre = "Juan"
n_edad = 30
f_estatura = 1.75
is_hombre = True #True y False llevan la primera letra en mayuscula
s_textoLargo = """Esto es un mensaje
...con tres saltos
...de linea"""

# Declaración de constante:
NUMEROPI = 3.14159

print(s_nombre, n_edad, f_estatura, is_hombre)

a, b, c = 'string', 15, True
# Sería como poner:
a = 'string'
b = 15
c = True

n_numero = n_edad

print('la variable n_numero tiene un valor de:',n_numero,' y apunta a ' ,id(n_numero), ' idual que la variable n_edad ', id(n_edad)) 


# Para verificar el tipo de cualquier objeto en Python, usamos la función type() :
print('n_edad es de tipo: ', type(n_edad))
print('n_numero es de tipo: ',type(n_numero))
print('s_nombre es de tipo: ',type(s_nombre))
print('NUMEROPI es de tipo: ',type(NUMEROPI))
print('is_hombre es de tipo: ',type(is_hombre))

# Forzado de tipo, CASTING:
# Forzado de tipo Enteros:
x = int(1) # x Valdrá 1
y = int(2.8) # y Valdrá 2
z = int("3") # z Valdrá 3
# Forzado de tipo Float:
x = float(1) # x Valdrá 1.0
y = float(2.8) # y Valdrá 2.8
z = float("3") # z Valdrá 3.0
w = float("4.2") # w Valdrá 4.2
# Forzado de tipo string:
x = str("s1") # x Valdrá 's1'
y = str(2) # y Valdrá '2'
z = str(3.0) # z Valdrá '3.0'
# CASTING. Reconversión de tipos:
# Casting de int a float:
n_numero = 13
n_numero_2 = float(n_numero)
# Casting de float a int:
n_numero_3 = 24.876
n_numero_4 = int(n_numero_3)
# Casting de string a int
s_texto = "13"
n_numero_5 = int(s_texto)
# Casting de int a string
n_numero_6 = 27
s_texto_2 = str(n_numero_6)
print('n_numero_2:',n_numero_2)
print('Es de tipo',type(n_numero_2))
print('n_numero_4:',n_numero_4)
print('Es de tipo',type(n_numero_4))
print('n_numero_5:',n_numero_5)
print('Es de tipo',type(n_numero_5))
print('s_texto_2:',s_texto_2)
print('Es de tipo',type(s_texto_2))


# Para concatenar textos se hace con “+” o simplemente con una coma.
# Si ponemos coma nos pone entre los textos un espacio, con + no lo hace.
print("Esta frase" , "termina aquí.")
print("Esta frase" + "termina aquí.")
# Contatenación y multiplicación de strings
a = "uno"
b = "dos"
c = a + b # c es "unodos"
print('a + b', c )
c = a * 3 # c es "unounouno"
print('a * 3', c )
#--------------------------------------
# MÉTODOS DE LOS STRINGS:
# lower(): Convierte en minúsculas un string.
s_texto1 = "ESTE TEXTO ESTÁ INICIALMENTE EN MAYÚSCULAS"
print(s_texto1.lower())
# capitalize(): Pone la primera letra en mayúscula.
s_texto2 = "este texto no tenía la primera letra en mayúsculas"
print(s_texto2.capitalize())
# count(): Cuenta cuantas veces aparece una letra o una cadena de caracteres.
s_texto3 = "Vamos a ver cuántas veces aparece la letra c"
print(s_texto3)
print('tiene',s_texto3.count('c'), 'letras c')
# find(): Representa el índice o la posición en el cual aparece un carácter o un grupo de caracteres. 
# Si aparece varias # veces me dice sólo el primero.
s_texto4 = "Vamos a ver en qué posición aparece primero la letra e"
print(s_texto4)
print('La letra "e" aparece en la posicion', s_texto4.find('e'))

# rfind(): Igual que find() pero contando desde atrás.
s_texto5 = "Vamos a ver en qué posición aparece la palabra desde, contando desde atrás"
print(s_texto5)
print('La palabra "desde" aparece en la posicion', s_texto5.rfind('desde'))
# isdigit(): Devuelve un boolean, nos dice si el valor introducido es un string. 
# Tiene que ser un valor introducido entre comillas o dará error.
s_texto6 = "6"
print('"6"',s_texto6.isdigit())
# isalum(): Devuelve un boolean, Devuelve verdadero si todos los caracteres de la 
# cadena son numéricos y hay al menos un carácter. En caso contrario, devuelve falso.
s_texto7 = "9857654gf7"
print( "9857654gf7", s_texto7.isalnum())
# isalpha(): Devuelve un boolean, comprueba si hay sólo letras. Los
# espacios no cuentan. 
s_texto8 = "Holamundo"
print("Holamundo", s_texto8.isalpha())
s_texto8 = "Hola mundo"
print("Hola mundo", s_texto8.isalpha())
# split(): Separa por palabras utilizando espacios. Crea una lista.
s_texto9 = "Vamos a separar esta frase por los espacios"
print("Vamos a separar esta frase por los espacios", s_texto9.split())
# Podemos usar otro carácter como separador, por ejemplo una coma:
s_texto10 = "Esta sería la primera parte,y esta la segunda"
print('separando por coma Esta sería la primera parte,y esta la segunda', s_texto10.split(","))
# strip(): Borra los espacios sobrantes al principio y al final.
s_texto11 = " En este texto había espacios al principio y al final "
print(" En este texto había espacios al principio y al final ", s_texto11.strip())
# replace(): Cambia una palabra o una letra por otra.
s_texto12 = "Vamos reemplazar la palabra casa"
print("Vamos reemplazar la palabra casa por hogar con replace", s_texto12.replace("casa", "hogar"))