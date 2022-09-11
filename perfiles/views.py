from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(('GET', 'POST'))
def UserProfile(request):
    data = {"test": "data"}
    return Response(data=data)