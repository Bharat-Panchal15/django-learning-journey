from django.shortcuts import render
from .models import Book

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request,'books/book_list.html',{'books':books})