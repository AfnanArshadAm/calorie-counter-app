from django.db import models
import uuid

from fooditem.models import LabelTag
from user.models import User



class UserFoodItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_food_item")
    food_name = models.CharField(max_length=100)
    calories = models.CharField(max_length=100)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.food_name


class UserActivity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_activity")
    activity_name = models.CharField(max_length=100)
    calories_burned = models.CharField(max_length=100)
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return self.activity_name



class Meal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_food_consumption")
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    food_consumed = models.ForeignKey(UserFoodItem,on_delete=models.CASCADE, related_name="user_food_item_consumed")
    amount_consumed = models.CharField(max_length=100)
    calories_consumed = models.CharField(max_length=100)


    def __str__(self):
        return self.title



class Workout(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="user_activity_log")
    date_added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    activiy_done = models.ForeignKey(UserActivity,on_delete=models.CASCADE, related_name="user_activities")
    time_spent = models.CharField(max_length=100)
    calories_burned_in_activity = models.CharField(max_length=100)



    def __str__(self):
        return self.title