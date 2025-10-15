from django.contrib import admin
from .models import Product, Order

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock','created_at')
    search_fields= ('name',)

admin.site.register(Product,ProductAdmin)
admin.site.register(Order)