from rest_framework import serializers
from .models import Supers

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        #super_type_id = serializers.IntegerField(write_only=True)
        model = Supers
        fields = [
        'id', 
        'name', 
        'alter_ego', 
        'primary_ability', 
        'secondary_ability', 
        'catchphrase', 
        'super_type',
        ]
        #depth = 1
