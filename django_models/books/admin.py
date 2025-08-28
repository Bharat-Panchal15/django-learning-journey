from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','published_date','is_published')
    list_filter = ('published_date','is_published')
    search_fields = ('title','author')

admin.site.register(Book,BookAdmin)