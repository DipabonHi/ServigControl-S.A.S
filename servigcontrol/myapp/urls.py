from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('contact/', views.contact, name="contact"),
    path('crear_usuario/', views.crear_usuario, name= 'crear_usuario'),
    path('turnos/', views.turnos, name="turnos"),
    path('turnos_completos/', views.turnos_completos, name="turnos_completos"),
    path('turno/crear/', views.crear_turno, name="crear_turno"),
    path('turno/<int:turno_id>/', views.datalle_turno, name="detalle_turno"),
    path('turno/<int:turno_id>/eliminar/', views.eliminar_turno, name="eliminar_turno"),
    path('turno/<int:turno_id>/completar/', views.completar_turno, name="completar_turno"),
]

