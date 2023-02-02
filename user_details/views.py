import datetime

from django.db.models.aggregates import Sum
from rest_framework import status
from rest_framework.decorators import (api_view, parser_classes,
                                       permission_classes)
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from calorie_counter.permissions import IsAdmin

from .models import *
from .serializers import *


class UserFoodItemViewSet(ModelViewSet):
    queryset = UserFoodItem.objects.all()
    serializer_class = UserFoodItemSerializer

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH' or self.request.method == 'DELETE':
            permission_classes = [IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        user = User.objects.get(id=self.request.user.id)
        if user.is_admin:
            data["is_approved"]="true"
        else:
            data["user"]=user.id
            data["is_approved"]=False
        
        serializer = self.get_serializer(data=data, context={'request': self.request})
        if(serializer.is_valid()):
            self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if self.request.GET.get("is_approved") and self.request.GET.get("user"):
            is_approved = self.request.GET.get("is_approved")
            user = self.request.GET.get("user")
            if request.user.is_admin :
                queryset = queryset.filter(is_approved=is_approved,user=user)
                serializer = self.get_serializer(queryset,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if self.request.GET.get("is_approved"):
            is_approved = self.request.GET.get("is_approved")
            if request.user.is_admin :
                queryset = queryset.filter(is_approved=is_approved)
                serializer = self.get_serializer(queryset,many=True)
            elif not request.user.is_admin :
                queryset = queryset.filter(user=request.user,is_approved=is_approved)
                serializer = self.get_serializer(queryset,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else :
            if request.user.is_admin :
                queryset = queryset.filter(is_approved=True)
                serializer = self.get_serializer(queryset,many=True)
            elif not request.user.is_admin :
                queryset = queryset.filter(user=request.user,is_approved=True)
                serializer = self.get_serializer(queryset,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)








class UserActivityViewSet(ModelViewSet):
    queryset = UserActivity.objects.all()
    serializer_class = UserActivitySerializer


    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH' or self.request.method == 'DELETE':
            permission_classes = [IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        user = User.objects.get(id=self.request.user.id)
        if user.is_admin:
            data["is_approved"]="true"
        else:
            data["user"]=user.id
            data["is_approved"]=False
        
        serializer = self.get_serializer(data=data, context={'request': self.request})
        if(serializer.is_valid()):
            self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if self.request.GET.get("is_approved") and self.request.GET.get("user"):
            is_approved = self.request.GET.get("is_approved")
            user = self.request.GET.get("user")
            if request.user.is_admin :
                queryset = queryset.filter(is_approved=is_approved,user=user)
                serializer = self.get_serializer(queryset,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if self.request.GET.get("is_approved"):
            is_approved = self.request.GET.get("is_approved")
            if request.user.is_admin :
                queryset = queryset.filter(is_approved=is_approved)
                serializer = self.get_serializer(queryset,many=True)
            elif not request.user.is_admin :
                queryset = queryset.filter(user=request.user,is_approved=is_approved)
                serializer = self.get_serializer(queryset,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else :
            if request.user.is_admin :
                queryset = queryset.filter(is_approved=True)
                serializer = self.get_serializer(queryset,many=True)
            elif not request.user.is_admin :
                queryset = queryset.filter(user=request.user,is_approved=True)
                serializer = self.get_serializer(queryset,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)




class MealViewSet(ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]


    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        if not self.request.user.is_admin:
            data["user"] = self.request.user.id
        user_food_item_calories = UserFoodItem.objects.get(id = data["food_consumed"]).calories
        data["calories_consumed"]=int(user_food_item_calories)*int(data["amount_consumed"])
        serializer = self.get_serializer(data=data, context={'request': self.request})
        if(serializer.is_valid()):
            self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)




class WorkoutViewSet(ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]


    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        if not self.request.user.is_admin:
            data["user"] = self.request.user.id
        user_activity_calories_burned = UserActivity.objects.get(id = data["activiy_done"]).calories_burned
        data["calories_burned_in_activity"]=int(user_activity_calories_burned)*int(data["time_spent"])
        serializer = self.get_serializer(data=data, context={'request': self.request})
        if(serializer.is_valid()):
            self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)






@api_view(['GET',])
@permission_classes((IsAuthenticated,))
@parser_classes([JSONParser,])
def user_statistics(request):
    if request.GET.get("statistics")=="daily" :
        context = {}
        today = datetime.date.today()
        meals = Meal.objects.filter(date_added__date=today,user=request.user).aggregate(calories_consumed=Sum('calories_consumed'))
        context["calories_consumed"]=meals["calories_consumed"]

        workout = Workout.objects.filter(date_added__date=today,user=request.user).aggregate(calories_burned=Sum('calories_burned_in_activity'))
        context["calories_burned"]=workout["calories_burned"]
        return Response(context,status=status.HTTP_200_OK)

    if request.GET.get("statistics")=="weekly" :
        context = {}
        today = datetime.date.today()
        starting_day = today - datetime.timedelta(7)
        print("today",today)
        print("starting_day",starting_day)

        meals = Meal.objects.filter(date_added__gte=starting_day,user=request.user).aggregate(calories_consumed=Sum('calories_consumed'))
        context["calories_consumed"]=meals["calories_consumed"]

        workout = Workout.objects.filter(date_added__gte=starting_day,user=request.user).aggregate(calories_burned=Sum('calories_burned_in_activity'))
        context["calories_burned"]=workout["calories_burned"]
        return Response(context,status=status.HTTP_200_OK)
    
    if request.GET.get("statistics")=="monthly" :
        context = {}
        today = datetime.date.today()
        starting_day = today - datetime.timedelta(30)
        print("today",today)
        print("starting_day",starting_day)

        meals = Meal.objects.filter(date_added__gte=starting_day,user=request.user).aggregate(calories_consumed=Sum('calories_consumed'))
        context["calories_consumed"]=meals["calories_consumed"]

        workout = Workout.objects.filter(date_added__gte=starting_day,user=request.user).aggregate(calories_burned=Sum('calories_burned_in_activity'))
        context["calories_burned"]=workout["calories_burned"]
        return Response(context,status=status.HTTP_200_OK)


