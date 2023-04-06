from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from AppCoder_2.forms import UserRegisterForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def login_request(request):
    if request.method == 'POST':
        if 'login_invitado' in request.POST:
            # Autenticar un usuario invitado
            username = 'invitado'
            password = 'invitado123'
            user = authenticate(username=username, password=password)
            return render(request,"inicio_invitado.html", {"mensaje":"Usted a ingresado como invitado Bienvenido!", "invitado": True})
        else:
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                usuario = form.cleaned_data.get('username')
                contra = form.cleaned_data.get('password')
                user = authenticate(username=usuario, password=contra)
                if user is not None:
                    login(request, user)
                    return render(request,"inicio.html",  {"mensaje":f"Bienvenido {usuario} :)", "invitado": False} )
                else:
                    return render(request, "login2.html", {"form": form, "mensaje": "Error, datos incorrectos"})
            else:
                return render(request, "login2.html", {"form": form, "mensaje": "Error, formulario erroneo"})
    else:
        form = AuthenticationForm()
        return render(request, "login2.html", {"form": form})      
              
def login_invitado(request):
    return render(request, 'inicio_invitado.html')

def register(request):

        if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request,"inicio.html")
            
            
        else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     
            return render(request,"registro.html" ,  {"form":form})

