from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from rest_framework.views import APIView,Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.

@api_view(['POST'])
def Signup(request):
    serial=UserSerializer(data=request.data)
    if serial.is_valid():
        serial.save()
        user= User.objects.get(username=request.data['username'])
        return Response({'user':serial.data})
    else:
        return Response({'msg':serial.errors},status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def Login(request):
    user= get_object_or_404(User,username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({'details':'not found'}, status=status.HTTP_404_NOT_FOUND)
    serialize=UserSerializer(instance=user)
    return Response(status=status.HTTP_200_OK)
        

class DocRegister(APIView):
    def post(self,request,*args,**kwargs):
        try:
            doc=DocSerializer(data=request.data)
            if doc.is_valid():
                doc.save()
                return Response(data=doc.data)
            else:
                return Response({'msg':doc.errors},status=status.HTTP_404_NOT_FOUND)
        except:
                return Response({'msg':'failed'},status=status.HTTP_404_NOT_FOUND)
    def get(self,request,*args,**kwargs):
        dishes=Doctor.objects.all()
        dish_serialize=DocSerializer(dishes,many=True)
        return Response(data=dish_serialize.data)
                



