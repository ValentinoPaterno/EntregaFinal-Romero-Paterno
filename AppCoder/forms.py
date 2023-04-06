from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)

class EstudiantesFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class EntregableFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    fecha_De_Entrega = forms.DateField()
    entregado = forms.BooleanField()
    imagen = forms.ImageField()

class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir cotraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Ingrese su email: ")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir cotraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2','last_name', 'first_name']
        help_texts = {k:"" for k in fields}

class AvatarFormulario(forms.Form):
    username = forms.ModelChoiceField(queryset=User.objects.all())
    image = forms.ImageField(required=True)