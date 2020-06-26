# django
from django.urls import path, include
# rest framework
from rest_framework.routers import DefaultRouter
# apps
from users import views

router = DefaultRouter()
router.register(r'users/log', views.CircleViewSet, basename='cirlcle')



urlpatterns = [
    path('user/login/', views.UserLoginAPIView.as_view(), name='login'),
    path('user/signup/', views.UserSignupAPIView.as_view(), name='login'),
    path('', include(router.urls), name='login'),
]
