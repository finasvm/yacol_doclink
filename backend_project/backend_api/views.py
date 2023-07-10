from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from rest_framework.views import APIView,Response
from .serializers import *
from .models import *
from rest_framework import status

# Create your views here.

class UserRegister(APIView):
    def post(self,request,*args,**kwargs):
        try:
            user=UserSerializer(data=request.data)
            if user.is_valid():
                user.save()
                return Response(data=user.data)
            else:
                return Response({'msg':user.errors},status=status.HTTP_404_NOT_FOUND)
        except:
                return Response({'msg':'failed'},status=status.HTTP_404_NOT_FOUND)
        

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
                



