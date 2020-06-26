from django.urls import path, include
# apps
from users import views

urlpatterns = [
    path('user/login', views.UserLoginAPIView.as_view(), name='login'),
    path('user/signup', views.UserSignupAPIView.as_view(), name='login'),
]
