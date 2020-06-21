"""user views"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# models
from user.models import User, Profile

# serializers
from user.serializers import UserLoginSerializer

@csrf_exempt
# @method_decorator(csrf_exempt, name='dispatch')
class UserLoginAPIView(APIView):
    """user api login"""
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'status': 'ok',
            'token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
