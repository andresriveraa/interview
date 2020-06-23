from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(
        'email adress',
        unique=True,
        error_messages={
            'unique': 'El usuario ya existe'
        }
    )

    phone_number = models.CharField(max_length=17, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    created = models.DateTimeField(
        'create at ',
        auto_now_add=True,
        help_text='date time on create'
    )

    modified = models.DateTimeField(
        'create at ',
        auto_now=True,
        help_text='date time on modified'
    )

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username


from django.db import models

# Create your models here.
