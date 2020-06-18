from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# models
from user.models import User, Profile


class CustomUserAdmin(UserAdmin):
    last_display = ('email', 'username', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_client', 'is_staff', 'created', 'modified')


# admin.site.register(User)
# admin.site.register(Profile)
