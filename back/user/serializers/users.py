"""user serializers"""
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from user.models import User


# model serializer
class UserModelSerializer(serializers.ModelSerializer):
    model = User
    fields = (
        'username',
        'first_name'
    )


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credential')
        self.context['user'] = user
        return data

    def create(self, data):
        # token, created = Token.generate_key(user=self.context['user'])
        token = Token.generate_key()
        print(token)
        return self.context['user'], token.key
        # return self.context['user']
