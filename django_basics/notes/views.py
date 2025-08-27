from django.shortcuts import render
from django.contrib.auth.models import AnonymousUser
from datetime import date

# Create your views here.
def home(request):
    user = request.user if request.user.is_authenticated else AnonymousUser()

    items = ["Django","flask","FastAPI"]

    context = {
        "user": user,
        "items": items,
        "now": date.today()
    }
    return render(request,"home.html", context)

def profile(request):
    user = request.user if request.user.is_authenticated else AnonymousUser()

    hobbies = ["Programming","Cube solving","mathematics"]

    context = {
        "user":user,
        "hobbies":hobbies,
        "now": date.today()
    }
    return render(request,'profile.html',context)