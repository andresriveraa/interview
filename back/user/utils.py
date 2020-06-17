from django.db import models

class User_model(models.Model):
    """
    base para crear los usuarios
    """
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

    class Meta:
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']