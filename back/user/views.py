from rest_framework.decorators import api_view
from rest_framework.response import Response
# models
from user.models import User, Profile
# Create your views here.


@api_view(['GET'])
def hello(request):
    # userss = User.objects.all()
    profiles = Profile.objects.all()
    data = []
    for usr in profiles:
        data.append({
            'clicks': usr.biography
        })
    return Response(data)
