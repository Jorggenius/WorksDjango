from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_estudiantes, name='lista_estudiantes'),
    path('nuevo/', views.agregar_estudiante, name='agregar_estudiante'),
    path('editar/<int:estu_id>/', views.editar_estudiante, name='editar_estudiante'),
    path('eliminar/<int:estu_id>/', views.eliminar_estudiante, name='eliminar_estudiante'),

]
