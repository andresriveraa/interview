from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from users.models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'email'
        )


class UserSerializers(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=30)

    def validate(self, validated_data):
        user = authenticate(username=validated_data['email'], password=validated_data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credential')
        self.context['user'] = user
        return validated_data

    def create(self, validated_data):
        token, created = Token.objects.get_or_create(user=self.context['user'])
        user = self.context['user']
        return user, token.key
