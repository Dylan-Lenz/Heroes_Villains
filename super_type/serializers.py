from rest_framework import serializers
from .models import Super_type
from super.serializer import SuperSerializer

class SuperTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super_type
        fields = [
            'id', 
            'type'
        ]