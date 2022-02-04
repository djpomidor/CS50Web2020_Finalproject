from django.contrib import admin
from .models import User

class UsersAdmin(admin.ModelAdmin):
    list_users = ("id", "name")

# Register your models here.
admin.site.register(User, UsersAdmin)
