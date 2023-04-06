from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

from AppCoder import views



app_name = "AppCoder"

urlpatterns = [
    # Secciones
    path('login/', include('AppCoder_2.urls') ),
    path('inicio', views.inicio, name='Inicio'),
    path('cursos', views.cursos, name='Cursos'),
    path('estudiantes', views.estudiantes, name='Estudiantes'),
    path('profesores', views.profesores, name='Profesores'),
    path('entregables', views.entregables, name='Entregables'),
    path('about', views.aboutus, name='About_Us'),
    # Funciones
    path('buscar/', views.buscar), # Busqueda de camadas
    path('curso/list', views.CursoList.as_view(), name='List'),
    path('<int:pk>', views.CursoDetalle.as_view(), name='Detail'),
    path('nuevo', views.CursoCreacion.as_view(), name='New'),
    path('editar/<int:pk>', views.CursoUpdate.as_view(), name='Edit'),
    path('borrar/<int:pk>', views.CursoDelete.as_view(), name='Delete'),
    # Register y Login
    #path('register', views.register, name= 'Register'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='Logout'),
    
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
    path('agregarAvatar', views.agregarAvatar, name='AgregarAvatar'),
    path('proximamente', views.proximamente, name='Proximamente'),

]