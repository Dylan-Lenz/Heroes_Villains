from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import SuperSerializer
from .models import Supers

@api_view(['GET', 'POST'])
def super_list(request):
    
    if request.method == 'GET':    
        super = Supers.objects.all()
        serializer = SuperSerializer(super, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def super_detail(request, pk):
    try:
        super = Supers.objects.get(pk=pk)
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    except Supers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
