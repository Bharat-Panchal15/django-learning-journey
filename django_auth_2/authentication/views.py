from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegistrationForm

# Create your views here.

def home_view(request):
    return render(request,'user/home.html')

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = User.objects.create_user(username=username,password=password)
            login(request,user)
            return redirect('profile')
    else:
        form = RegistrationForm()
    return render(request,'accounts/register.html',{'form':form})

def login_view(request):
    error_msg = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            next_url = request.POST.get("next") or request.GET.get("next") or "profile"
            return redirect(next_url)
        else:
            error_msg = "Invalid Credentials"
    return render(request,"accounts/login.html",{'error':error_msg})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
    else:
        return redirect('profile')

@login_required
def profile_view(request):
    return render(request,'user/profile.html')