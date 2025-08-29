# from django.contrib import admin

# # Register your models here.
# from django.contrib.auth import User 
# from django.contrib.auth.admin import UserAdmin

# @admin.register(User)
# class NewAdmin(UserAdmin):
#     readonly_fields = [
#         'date_joined',
#     ]
from django.contrib import admin

from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("user_name", "email", "age")
    search_fields = ("user_name__startswith",)