from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from calorie_counter.permissions import IsAdmin

from .models import *
from .serializers import *


class FoodItemViewSet(ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    permission_classes = [IsAdmin]



class LabelTagViewSet(ModelViewSet):
    queryset = LabelTag.objects.all()
    serializer_class = LabelTagSerializer
    permission_classes = [IsAuthenticated]
    permission_classes = [IsAdmin]

