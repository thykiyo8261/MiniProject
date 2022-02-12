from django.contrib import admin
from django.urls import path

from Accounts.views import logout_view, register_view, login_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout')
]