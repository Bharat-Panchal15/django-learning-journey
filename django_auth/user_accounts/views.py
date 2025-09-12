from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm

# Create your views here.

@login_required
def home(request):
    return render(request,"home.html")

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Create User but don't save password as plain text
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password']) # hash password
            user.save()
            return redirect("log_in")
    else:
        form = SignUpForm()
    return render(request,"signup.html",{'form':form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            identity = form.cleaned_data.get("identity")
            password = form.cleaned_data.get("password")

            user = authenticate(request, identity=identity, password=password)

            if user is not None:
                login(request,user)
                return redirect("home")
            else:
                form.add_error(None,"Invalid identity or password")
    else:
        form = LoginForm()
    return render(request,"login.html",{'form':form})

def logout_view(request):
    logout(request)
    return redirect("log_in")