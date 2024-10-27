from django.urls import path
from .views import * 

urlpatterns = [
    path('accounts', account_list, name='account-list'),
    path('accounts/<int:id>/', account_detail, name='account-detail'), 
    path('accounts/register', register, name='account-register'),
    path('accounts/login', login, name='account-login'),
    path('accounts/profile', profile, name='account-profile'),
]
