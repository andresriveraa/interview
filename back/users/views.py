import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
# serializers
from users.serializers import (
    UserLoginSerializers,
    UserModelSerializer,
    UserSignupSerializers
)
from users.models import User


class UserLoginAPIView (APIView):

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializers(data=request.data)
        if serializer.is_valid():
            user, token = serializer.save()
            print(user)
            data ={
                'user': UserModelSerializer(user).data,
                'token': token,
            }
            return Response(data, status=status.HTTP_201_CREATED)
        data = 'bad request'
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


class UserSignupAPIView (APIView):

    def post(self, request, *args, **kwargs):
        serializer = UserSignupSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            data ={
                'user': UserModelSerializer(user).data,
            }
            return Response(data, status=status.HTTP_201_CREATED)
        data = 'bad request'
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

