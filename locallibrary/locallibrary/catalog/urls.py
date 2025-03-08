from django.urls import path
from . import views
from catalog.views import  welcome


urlpatterns = [
       path('welcome/', welcome),
]