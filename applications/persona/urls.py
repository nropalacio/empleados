from django.contrib import admin
from django.urls import path

def graduacion(self):
    print('yay graduacion!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

urlpatterns = [
    path('persona/', graduacion),
]
