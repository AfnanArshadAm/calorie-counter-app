from rest_framework import serializers
from .models import *





class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity

        fields = [
            'id',
            'activity_name',
            'calories_burned',
        ] 


