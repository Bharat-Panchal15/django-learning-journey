from django.contrib import admin
from django.contrib.auth.models import User
from .models import Book, Review

# Register your models here.
admin.site.register(Book)
admin.site.register(Review)