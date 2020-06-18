from django.db import models


class Ingresa (models.Model):
    user_id = models.PositiveIntegerField(default=0)
    signIn = models.DateTimeField(
        'create at ',
        auto_now_add=True,
        help_text='date time on create'
    )

    time_in_app = models.DateTimeField(
        'create at ',
        auto_now=True,
        help_text='date time on modified'
    )