from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# models
from users.models import User


class CustomUserAdmin(UserAdmin):
    last_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_verified')
    list_filter = ('created', 'modified')


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     last_display = ('user', 'clicks', 'time_in_app')
#     search_filter = ('user__username', 'user__email', 'user__first_name', 'user__last_name')


admin.site.register(User, CustomUserAdmin)
