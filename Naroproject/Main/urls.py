from django.urls import path
from .views import main_af_login,home,answer

urlpatterns = [
    path('',home, name="main_bf_login"), #주소지정, 함수실행, 이름
    path('main_af_login/', main_af_login, name="main_af_login"),
    path('main_af_login/', answer, name="answer"),
]