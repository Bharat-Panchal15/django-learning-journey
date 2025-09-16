from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUser(UserAdmin):
    list_display = ('username','email','password','phone_number')
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields': ('phone_number',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields': ('phone_number',)}),
    )