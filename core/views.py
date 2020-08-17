from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .models import Buildings


# Create your views here.
@login_required(login_url='/login/')
def list_all_buildings(request):
    buildings = Buildings.objects.filter(active=True)
    return render(request, 'list.html', {'buildings':buildings})

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/login/')


@csrf_protect
def submit_user(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e/ou senha inválido. Tentar novamente!')
    return redirect('/login/')




