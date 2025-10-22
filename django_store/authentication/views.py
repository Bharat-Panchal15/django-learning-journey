from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.views import View
from .forms import RegistrationForm, LoginForm

# Create your views here.

class RegisterView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('product-list')
        
        form = RegistrationForm()
        return render(request,'authentication/register.html', {'form': form})
    
    def post(self,request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username,password=password)
            login(request,user)
            return redirect('product-list')
        return render(request,'authentication/register.html', {'form':form})

class LoginView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('product-list')
        
        form = LoginForm()
        return render(request,'authentication/login.html',{'form': form})
    
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username,password=password)

            if user is not None:
                login(request, user)
                return redirect('product-list')
            else:
                form.add_error(None,'Invalid credentials')
        return render(request,'authentication/login.html', {'form':form})

class LogoutView(View):
    def get(self,request):
        return render(request,'authentication/logout.html')
    
    def post(self,request):
        logout(request)
        return redirect('home')