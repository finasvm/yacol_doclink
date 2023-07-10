from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class DocSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields='__all__'


    