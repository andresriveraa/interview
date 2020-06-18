from rest_framework.decorators import api_view
from rest_framework.response import Response
# models
from user.models import User
# Create your views here.


@api_view(['GET'])
def hello(request):
    userss = User.objects.all()
    data = []
    for usr in userss:
        data.append({
            'name': usr.first_name
        })
    return Response(data)
