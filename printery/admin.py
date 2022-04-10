from django.contrib import admin
from .models import *

class UsersAdmin(admin.ModelAdmin):
    list_display = ("id", "username")

class OrdersAdmin(admin.ModelAdmin):
    list_display = ("number", "name", "type")

# Register your models here.
admin.site.register(User, UsersAdmin)
admin.site.register(Company)
admin.site.register(Paper)
admin.site.register(Order, OrdersAdmin)
admin.site.register(Part)
