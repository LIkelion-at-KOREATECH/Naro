from django.urls import path
from .views import main_af_login,home

urlpatterns = [
    path('',home, name="main_bf_login"),
    path('main_af_login/', main_af_login, name="main_af_login"),
]