from django.contrib import admin
from django.urls import path

def desdeApps(self):
    print('juela buena esa =================')

urlpatterns = [
    path('departamento/', desdeApps),
]
