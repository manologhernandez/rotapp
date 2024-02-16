from rest_framework import serializers
from rota.models import *
from django.contrib.auth.models import User 
from rest_flex_fields import FlexFieldsModelSerializer

class UserSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    
class CasesSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Cases
        fields = '__all__'

class RotaUserSerialzer(FlexFieldsModelSerializer):
    class Meta:
        model = RotaUser
        fields = '__all__'
        expandable_fields = {
            'user': UserSerializer
        }
