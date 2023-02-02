from django.urls import path
from rest_framework import routers
from .views import *
from . import views


app_name = 'fooditem'

router = routers.DefaultRouter()
router.register('food_item',views.FoodItemViewSet)
router.register('labeltag',views.LabelTagViewSet)



urlpatterns=[]


urlpatterns += router.urls