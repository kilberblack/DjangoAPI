from django.urls import path
from .views import account_list, account_detail  # Importamos la nueva vista

urlpatterns = [
    path('accounts', account_list, name='account-list'),
    path('accounts/<int:id>/', account_detail, name='account-detail'),  # Ruta para obtener, editar y eliminar un usuario por ID
]
