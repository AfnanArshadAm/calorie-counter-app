from rest_framework import serializers
from .models import *







class LabelTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabelTag

        fields = [
            'id',
            'label_name',
        ] 



class FoodItemSerializer(serializers.ModelSerializer):
    label_details = LabelTagSerializer(source='labels',read_only=True,many=True)
    class Meta:
        model = FoodItem

        fields = [
            'id',
            'food_name',
            'label_details',
            'labels',
            'calories',
            
        ] 


