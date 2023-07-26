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

class AppointSerializer(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields='__all__' 



class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Results
        fields = '__all__' 

class Doctor_Days_serializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor_Date
        fields = '__all__' 
