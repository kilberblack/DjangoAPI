from django.urls import path
from .views import * 

urlpatterns = [
    path('accounts', account_list, name='account-list'),
    path('accounts/<int:id>/', account_detail, name='account-detail'), 
    path('accounts/register', register, name='account-register'),
    path('accounts/login', login, name='account-login'),
    path('accounts/profile', profile, name='account-profile'),
    path('asignaturas/', asignatura_list, name='asignatura-list'),
    path('asistencias/<int:asignatura_id>/', asistencia_list, name='asistencia-list'),
    path('asistencias/usuario/<int:usuario_id>/', asistencia_por_usuario, name='asistencia-por-usuario'),
    path('asistencias/incrementar/<int:asignatura_id>/<int:usuario_id>/', incrementar_asistencia, name='incrementar-asistencia'),
]
