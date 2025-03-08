from django.http import HttpResponse
import datetime

def saludo(request):
    miFecha=datetime.datetime.now()
    return HttpResponse("Hola mundo")

#Definición de una vista para contenido dinámico
def fecha(request):
    miFecha=datetime.datetime.now()
    texto2 = """<html>
    <body>
    <h2>Fecha y hora actual: </h2>%s
    </body>
    </html>
    """ % miFecha
    return HttpResponse(texto2)

def calcEdad(request, year):
    edadActual=42
    periodo=year-2025
    edadFutura=edadActual+periodo
    documento="<html><body><h2>En el año%s tendrás %s años.</h2></body></html>"%(year, edadFutura)
    return HttpResponse(documento)
