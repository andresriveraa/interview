"""user views"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

from django.views.decorators.csrf import csrf_exempt

# serializers
from user.serializers import UserLoginSerializer, UserModelSerializer


class UserLoginAPIView(APIView):
    """user api login"""
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # user, token = serializer.save()
        data = {
            # 'status': UserModelSerializer(user).data,
            # 'token': token
            'status': 'hello',
            'token': 'world'
        }
        return Response(data, status=status.HTTP_201_CREATED)
        # return Response(UserLoginSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


def hello(APIView):
    data = 'hello'
    return Response(data)
