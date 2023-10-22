from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('buscar-alumno/', views.view_detalles_alumno,
         name='view_detalles_alumno'),
    path('detalles-alumno/',
         views.detalles_alumno, name='detalles_alumno'),
]