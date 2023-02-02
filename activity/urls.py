from django.urls import path
from rest_framework import routers
from .views import *
from . import views


app_name = 'activity'

router = routers.DefaultRouter()
router.register('activity',views.ActivityViewSet)



urlpatterns=[]


urlpatterns += router.urls