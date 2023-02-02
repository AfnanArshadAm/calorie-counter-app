from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import (api_view, parser_classes,
                                       permission_classes)
from rest_framework.parsers import FormParser, JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from activity.models import Activity

from calorie_counter.permissions import IsAdmin
from fooditem.models import FoodItem
from user_details.models import UserActivity, UserFoodItem

from .models import *
from .serializers import *


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': self.request})
        if(serializer.is_valid()):
            user = serializer.save()

            fooditems = FoodItem.objects.all().values()
            for item in fooditems : 
                UserFoodItem.objects.create(
                    user=user,
                    food_name = item["food_name"],
                    calories = item["calories"],
                    is_approved = True
                    )
                
            activities = Activity.objects.all().values()
            for item in activities : 
                UserActivity.objects.create(
                    user=user,
                    activity_name = item["activity_name"],
                    calories_burned = item["calories_burned"],
                    is_approved = True
                    )

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            data = {"error":serializer.errors}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)










@api_view(['POST'])
@permission_classes((AllowAny, ))
@parser_classes([JSONParser,FormParser])
def login_view(request):
    context = {}
    status_code=status.HTTP_400_BAD_REQUEST
    try:
        context = {}
        username = request.data.get('username')
        password = request.data.get('password')
        print("username",username)
        print("password",password)

        user = User.objects.get(username=username, password=password )
        print("user",user)
        if user:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            context['response'] = 'Successfully authenticated.'
            context['pk'] = user.pk
            context['username'] = username.lower()
            context['token'] = token.key
        else:
            context['response'] = 'Error'
            context['error_message'] = 'The username or password is incorrect'
        return Response(context)

    except:
        context['response'] = 'User not found !'
        status_code=status.HTTP_400_BAD_REQUEST   
    return Response(context,status=status_code)



    

@api_view(['POST',])
@permission_classes((AllowAny, ))
@parser_classes([JSONParser,FormParser])
def logout_view(request):
    context = {}
    try:
        request.user.auth_token.delete()
        context['response'] = 'LogOut Successful.'
        status_code=status.HTTP_200_OK
    except:
        context['response'] = 'Error'
        context['error_message'] = 'Invalid Token'
        status_code=status.HTTP_400_BAD_REQUEST
    
    return Response(context,status=status_code)