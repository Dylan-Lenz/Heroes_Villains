from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from super_type.models import Super_types
from .serializer import SuperSerializer
from .models import Supers

@api_view(['GET', 'POST'])
def super_list(request):
    if request.method == 'GET':    
        type_name = request.query_params.get('type')
        queryset = Supers.objects.all()
        serializer = SuperSerializer(queryset, many=True)
        if type_name:
            queryset = queryset.filter(super_type__type=type_name)
            serializer = SuperSerializer(queryset, many=True)
        elif type_name == 'Hero':
            queryset = queryset.filter(super_type__type=type_name)
            serializer = SuperSerializer(queryset, many=True)
        elif type_name == 'Villain':
            queryset = queryset.filter(super_type__type=type_name)
            serializer = SuperSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)