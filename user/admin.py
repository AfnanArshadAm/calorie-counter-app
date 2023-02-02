from django.contrib import admin
from .models import *



class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email','username','is_admin','is_active','full_name','phone')
admin.site.register(User,UserAdmin)
