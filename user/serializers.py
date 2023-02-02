
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User

        fields = [
            'email',
            'username',
            'password',
            'is_admin',
            'full_name',
            'phone'
        ] 





