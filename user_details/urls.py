from django.urls import path
from rest_framework import routers
from .views import *
from . import views


app_name = 'user_details'

router = routers.DefaultRouter()
router.register('user_food_item',views.UserFoodItemViewSet)
router.register('user_activity',views.UserActivityViewSet)

router.register('user_meal',views.MealViewSet)
router.register('user_workout',views.WorkoutViewSet)





urlpatterns=[
    path('user_statistics/', views.user_statistics),

]


urlpatterns += router.urls