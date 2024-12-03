from django.urls import path
from .views import * 

urlpatterns = [
    path('accounts', account_list, name='account-list'),
    path('accounts/<int:id>/', account_detail, name='account-detail'), 
    path('accounts/register', register, name='account-register'),
    path('accounts/login', login, name='account-login'),
    path('accounts/profile', profile, name='account-profile'),
    path('accounts/asignaturas/', asignatura_list, name='asignatura-list'),
    path('accounts/asignaturas/usuario/<int:usuario_id>/', asignatura_por_usuario, name='asignatura-por-usuario'),
    path('accounts/asistencia/<int:asignatura_id>/', asistencia_list, name='asistencia-list'),
    path('accounts/asistencia/usuario/<int:usuario_id>/', asistencia_por_usuario, name='asistencia-por-usuario'),
    path('accounts/asistencia/incrementar/<int:asignatura_id>/<int:usuario_id>/', incrementar_asistencia, name='incrementar-asistencia'),
    path('accounts/asignaturas/crear/', crear_asignatura, name='crear-asignatura'),
    path('accounts/asignaturas/asignar/<int:usuario_id>/<int:asignatura_id>/', asignar_asignatura_a_usuario, name='asignar-asignatura-a-usuario'),
]
