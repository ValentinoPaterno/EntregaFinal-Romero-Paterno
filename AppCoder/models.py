from django.db import models
from django.contrib.auth.models import User
# from AppCoder_2.forms import UserRegisterForm
# Create your models here.

class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Camada: {self.camada}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Profesion: {self.profesion}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_Entrega = models.DateField()
    entregado = models.BooleanField()
    imagen = models.ImageField(upload_to="images/", null=True, blank=True)

    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha de entrega: {self.fecha_de_Entrega} - Entregado {self.entregado} - Imagen {self.imagen}"  

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return (f'User: {self.user} || Imagen: {self.imagen}')