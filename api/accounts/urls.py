from django.urls import path
from .views import *

urlpatterns = [
    path('accounts', account_list, name='account-list'),
]