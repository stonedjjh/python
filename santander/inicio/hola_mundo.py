import datetime
print ("¡Hola, Mundo!")

edad = 60

if edad < 18:
    print ("Eres menor de edad")
elif edad >= 18 and edad < 60:
    print ("Eres un adulto")
elif edad > 15:
    print ("Mayor de 15 años")    
elif edad == 60:
    print ("Feliz 60 cumpleaños!")    
else:
    print ("Eres un adulto mayor.")


numero = 7

if numero % 2 == 0:
   

    resultado = "Par"

else:
    resultado = "Impar"

fecha_actual = datetime.datetime.now()    

print(fecha_actual)

print((not True) or (False and True) )

x = 5
y = "3"
z = x + int(y)
print(z)

s_texto6 = "6"
print(s_texto6.isdigit())

s_texto7 = "98576547.50"
print(s_texto7.isalnum())

s_texto9 = "Vamos a separar esta frase por los espacios"
print(s_texto9.split())

miNumero = 65
miNumero2 = miNumero
print("La dirección de memoria es" ,
id(miNumero))
print("La dirección de memoria es" ,
id(miNumero2))
miNumero = 70
print(miNumero2)
print("La dirección de memoria es" ,
id(miNumero))
print("La dirección de memoria es" ,
id(miNumero2))

a = 65
print("La dirección de memoria es" ,
id(a))
a+=2
print("La dirección de memoria es" ,
id(a))