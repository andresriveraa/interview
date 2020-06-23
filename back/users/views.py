import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
# serializers
from users.serializers import UserSerializers, UserModelSerializer
from users.models import User


class login (APIView):
    def get(self, request, *args, **kwargs):
        data = 'hello woerld'
        return Response(data, status=status.HTTP_201_CREATED)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializers(data=request.data)
        serializer.is_valid()
        user, token = serializer.save()
        print(token)
        data ={
            'user': UserModelSerializer(user).data,
            'token': token,
        }
        return Response(data, status=status.HTTP_201_CREATED)

