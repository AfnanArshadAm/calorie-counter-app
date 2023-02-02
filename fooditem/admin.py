from django.contrib import admin
from .models import *



class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('id','food_name','calories')
admin.site.register(FoodItem,FoodItemAdmin)

