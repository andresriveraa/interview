from django.db import models
# utils
from user.utils import UserModel


class Profile (UserModel):
    user = models.OneToOneField('user.User', on_delete=models.CASCADE)
    logo = models.ImageField(
        'profile picture',
        upload_to='users/picture',
        blank=True,
        null=True
    )

    biography = models.TextField(max_length=500, blank=True)

    clicks = models.PositiveIntegerField(default=0)
    time_in_app = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.user)
