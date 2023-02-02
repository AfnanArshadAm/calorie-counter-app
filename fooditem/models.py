from django.db import models
import uuid


class LabelTag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.label_name




class FoodItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    labels=models.ManyToManyField(LabelTag)
    food_name = models.CharField(max_length=100, unique=True)
    calories = models.CharField(max_length=100)

    def __str__(self):
        return self.food_name

