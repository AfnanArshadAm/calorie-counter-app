
from rest_framework import serializers
from .models import *




class UserFoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFoodItem

        fields = [
            'id',
            'user',
            'food_name',
            'calories',
            'is_approved'
        ] 



class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity

        fields = [
            'id',
            'user',
            'activity_name',
            'calories_burned',
            'is_approved'
        ] 




class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal

        fields = [
            'id',
            'date_added',
            'user',
            'title',
            'food_consumed',
            'amount_consumed',
            'calories_consumed'
        ] 



class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout

        fields = [
            'id',
            'date_added',
            'user',
            'title',
            'activiy_done',
            'time_spent',
            'calories_burned_in_activity'
        ] 