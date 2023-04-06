from django.urls import path
from django.contrib.auth.views import LogoutView
from AppCoder_2 import views

app_name= "AppCoder_2"
urlpatterns = [
    path('', views.login_request, name='login2'),
    path('register', views.register, name='Register'),
    path('inicio_invitado', views.login_invitado, name='Inicio_Invitado'),
]