from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import crear_turno_form
from .models import Turno
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'myapp/index.html')
    
def about(request):
    return render(request, 'myapp/about.html')
    
def services(request):
    return render(request, 'myapp/services.html')
    
def contact(request):
    return render(request, 'myapp/contact.html')

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'myapp/iniciar_sesion.html',{
            'form' : AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'myapp/iniciar_sesion.html',{
                'form' : AuthenticationForm,
                'error' : "Usuario o Contraseña incorrecta"
            })
        else:
            login(request, user)
            return redirect('principal')
        
@login_required        
def principal(request):
    return render(request, 'myapp/principal.html')

@login_required        
def cerrar_sesion(request):
    logout(request)
    return redirect('index')
    
@login_required        
def crear_usuario(request):
    if request.method == 'GET':
        return render(request, 'myapp/crear_usuario.html',{
            'form' : UserCreationForm
        })
    else:
        try:
            user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
            user.save()
            login(request, user)
            return redirect('principal')
        except IntegrityError:
            return render(request, 'myapp/crear_usuario.html',{
                'form' : UserCreationForm,
                "error" : 'El usuario ya existe'
            })
                
@login_required        
def turnos(request):
    turnos = Turno.objects.all()
    return render(request, 'myapp/turnos/turnos.html',{
        'turnos' : turnos
    })

@login_required    
def turnos_completos(request):
    turnos = Turno.objects.filter(fecha_completada__isnull=False).order_by('-fecha_completada')
    return render(request, 'myapp/turnos/turnos.html',{
        'turnos' : turnos
    })          

@login_required
def crear_turno(request):
    if request.method == 'GET':
        return render(request, 'myapp/turnos/crear_turno.html', {
            'form' : crear_turno_form
        })
    else:
        try:
            form = crear_turno_form(request.POST)
            nuevo_turno = form.save(commit=False)
            nuevo_turno.user = request.user
            nuevo_turno.save()
            return redirect('turnos')
        except ValueError:
            return render(request, 'myapp/turnos/crear_turno.html', {
                'form' : crear_turno_form,
                'error' : 'Ingresa datos validos'
            })
            
@login_required            
def datalle_turno(request, turno_id):
    if request.method == 'GET':
        turno = get_object_or_404(Turno, pk=turno_id)
        form = crear_turno_form(instance=turno)
        return render(request, 'myapp/turnos/detalle_turno.html',{
            'turno' : turno,
            'form' : form
        })
    else:
        try:
            turno = get_object_or_404(Turno, pk=turno_id)
            form = crear_turno_form(request.POST, instance=turno)
            form.save()
            return redirect('turnos')
        except ValueError:
            return render(request, 'myapp/turnos/detalle_turno.html',{
            'turno' : turno,
            'form' : form,
            'error' : "Error al actualizar"
        })
            
@login_required    
def eliminar_turno(request, turno_id):
    turno = get_object_or_404(Turno, pk=turno_id)
    if request.method == 'POST':
        turno.delete()
        return redirect('turnos')
    
@login_required                    
def completar_turno(request, turno_id):
    turno = get_object_or_404(Turno, pk=turno_id)
    if request.method == 'POST':
        turno.fecha_completada = timezone.now()
        turno.save()
        return redirect('turnos')
    
