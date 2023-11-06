from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser

admin.site.register(CustomUser)
"""  
from django.contrib import admin
from .models import MyUsers

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'user_type', 'is_active', 'is_staff')
    list_filter = ('is_active', 'user_type')
    search_fields = ('email', 'first_name', 'last_name')

admin.site.register(MyUsers, CustomUserAdmin) """