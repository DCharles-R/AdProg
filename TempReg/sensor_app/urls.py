from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('lista/', views.lista_lecturas, name='lista_lecturas'),
    path('agregar/', views.agregar_lecturas, name='agregar_lecturas'),
    path('buscar/', views.buscar_lectura, name='buscar_lecturas'),
    path('eliminar/<int:pk>/', views.eliminar_lecturas, name='eliminar_lecturas'),
    path('actualizar/<int:pk>/', views.modificar_lecturas, name='modificar_lecturas'),
    path('save_reading/<int:pk>/', views.leer_dato_Pi, name='sensor_read')
]