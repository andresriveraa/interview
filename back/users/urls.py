from django.contrib import admin
from django.urls import path, include
# apps
from users import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('user/login', views.login.as_view(), name='login')
]
