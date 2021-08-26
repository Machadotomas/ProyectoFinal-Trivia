from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import UserRegisterForm




def base(request):
    return render(request,"base.html",{})

def ingreso(request):
    return render(request,"ingreso.html",{})

def comojugar(request):
    return render(request,"comojugar.html",{})

def registro(request):
    return render(request,"registro.html",{})

def register(request):
    if request.method=='POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('base')
    else:
        form = UserRegisterForm()
    
    context=  { 'form' : form }
    return render(request, 'register.html', context)