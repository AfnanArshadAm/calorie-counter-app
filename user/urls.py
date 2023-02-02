from django.urls import path
from rest_framework import routers
from .views import *
from . import views


app_name = 'user'

router = routers.DefaultRouter()
router.register('user',views.UserViewSet, basename='user')


urlpatterns=[

    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
]


urlpatterns += router.urls