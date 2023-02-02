from django.contrib import admin
from .models import *



class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id','activity_name','calories_burned')
admin.site.register(Activity,ActivityAdmin)
