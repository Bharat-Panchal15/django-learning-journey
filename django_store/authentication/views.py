from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm

# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('product-list')
    
    else:
        form = RegistrationForm()
    return render(request,"authentication/register.html",{'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('product-list')
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = LoginForm()
    return render(request,"authentication/login.html",{'form': form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
    else:
        return render(request,'authentication/logout.html')