"""Users URLs."""
from django.urls import include, path
# apps
from user.views import UserLoginAPIView, hello

urlpatterns = [
    path('users/login', UserLoginAPIView.as_view(), name='login')
    # path('users/login', hello)
]
