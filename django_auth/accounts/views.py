from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SigUpForm

# Create your views here.

def home(request):
    return render(request,"base.html")

def sign_up(request):
    if request.method == "POST":
        form = SigUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            user = User.objects.create_user(username=username,email=email,password=password)
            return redirect("log_in")
    else:
        form = SigUpForm()
    return render(request,"signup.html",{'form':form})

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            return render(request,"login.html",{ "error": "Invalid credentials"})
    
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("log_in")