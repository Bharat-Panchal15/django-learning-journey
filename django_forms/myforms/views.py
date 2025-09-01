from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, ContactForm

# Create your views here.

def show_post(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts':posts})

def create_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'create_post.html',{'form':form})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            message = form.cleaned_data.get("message")

            print("Contact Form Submitted:",name,email,message)

            return render(request,"contact_success.html",{'name':name})
    form = ContactForm()
    return render(request,'contact.html',{'form':form})  