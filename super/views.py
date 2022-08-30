from unittest import TextTestRunner
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import SuperSerializer
from .models import Supers

@api_view(['GET'])
def super_list(request):
    super = Supers.objects.all()
    serializer = SuperSerializer(super, many=True)
    return Response(serializer.data)