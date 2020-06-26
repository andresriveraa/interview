# django
from django.contrib.auth import authenticate, password_validation
# rest_framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.authtoken.models import Token
# models
from users.models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'email'
        )


class UserSignupSerializers(serializers.Serializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())],
        max_length=40
    )
    password = serializers.CharField(max_length=128)
    password_confirmation = serializers.CharField(max_length=128)

    def validate(self, data):
        passwd = data['password']
        passwd_chek = data['password_confirmation']
        if passwd != passwd_chek:
            raise serializers.ValidationError('invalid credentials')
        password_validation.validate_password((passwd))
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        user = User.objects.create_user(**validated_data, is_verified=False)
        self.send_confirmation_email(validated_data['email'])

        return user

    def send_confirmation_email(self, user):
        """send acount verificartion"""
        verification_token = self.gen_verificarion_token(user=user)
        print('sending email')

    def gen_verificarion_token(self, user):
        """create jwt token that"""
        return 'abc'


class UserLoginSerializers(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=30)

    def validate(self, validated_data):
        user = authenticate(username=validated_data['email'], password=validated_data['password'])
        if not user:
            raise serializers.ValidationError('Invalid credential')
        if not user.is_verified:
            raise serializers.ValidationError('account is not active yer')
        self.context['user'] = user
        return validated_data

    def create(self, validated_data):
        token, created = Token.objects.get_or_create(user=self.context['user'])
        user = self.context['user']
        return user, token.key
