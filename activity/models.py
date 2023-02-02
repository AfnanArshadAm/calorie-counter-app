from django.db import models
import uuid





class Activity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    activity_name = models.CharField(max_length=100, unique=True)
    calories_burned = models.CharField(max_length=100)

    def __str__(self):
        return self.activity_name