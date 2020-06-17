"""user models"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# utils
from user.utils import User_model


class User (User_model, AbstractUser):
    email = models.EmailField(
        'email adress',
        unique=True,
        error_messages={
            'unique': 'El usuario ya existe'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='phone number be entered'
    )

    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client',
        default=True,
        help_text='clients are the main type of user'
    )

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='cuando esta verificado'
    )

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username
