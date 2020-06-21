from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# models
from user.models import User, Profile
# Create your views here.

# serializers
from user.serializers import UserLoginSerializer

@api_view(['GET'])
def hello(request):
    userss = User.objects.all()
    profiles = Profile.objects.all()
    data = []
    for usr in profiles:
        data.append({
            'clicks': usr.biography
        })
    return Response(data)