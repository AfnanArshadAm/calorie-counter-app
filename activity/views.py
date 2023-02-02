from rest_framework.viewsets import ModelViewSet

from calorie_counter.permissions import IsAdmin

from .models import *
from .serializers import *






class ActivityViewSet(ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAdmin]


