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
import json

# Create your views here.

@api_view(['POST'])
def Signup(request):
    serial=UserSerializer(data=request.data)
    if serial.is_valid():
        serial.save()
        # user= User.objects.get(username=request.data['username'])
        return Response({'user':serial.data})
    else:
        return Response({'msg':serial.errors},status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def Appointments(request):
    serial=AppointSerializer(data=request.data)
    if serial.is_valid():
        serial.save()
        # user= User.objects.get(username=request.data['username'])
        return Response({'user':serial.data,'details':'success'})
    else:
        return Response({'msg':serial.errors},status=status.HTTP_404_NOT_FOUND)





@api_view(['POST'])
def Login(request):
    user= get_object_or_404(User,username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({'details':'not found'}, status=status.HTTP_404_NOT_FOUND)
    user_id=user.id
    serialize=UserSerializer(instance=user)
    return Response({'msg':'success','user_id':user_id},status=status.HTTP_200_OK)
        

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
    
@api_view(['GET'])  
def all_appointments(request):
    appointments=Appointment.objects.all()
    serialized_data = []
    for appointment in appointments:
        appointment_data = AppointSerializer(appointment).data
        doctor_id = appointment_data.pop('doc')
        doctor = Doctor.objects.get(id=doctor_id)
        doctor_serializer = DocSerializer(doctor)
        appointment_data['doctor'] = doctor_serializer.data
        serialized_data.append(appointment_data)
    
    return Response(data=serialized_data)
    
    
@api_view(['GET'])  
def All_Result(request,*args,**kwargs):
    allresults=Results.objects.all()
    result_ser=ResultSerializer(allresults,many=True)
    return Response(data=result_ser.data)

@api_view(['GET'])  
def Doc_Dates(request,*args,**kwargs):
    doc_days=Doctor_Date.objects.all()
    result = []
    for doctor_date in doc_days:
        list_date = json.loads(doctor_date.List_date)
        list_day = json.loads(doctor_date.List_day)
        list_time = json.loads(doctor_date.List_time)

        # Serialize the data
        result.append({
                "id": doctor_date.id,
                "List_date": list_date,
                "List_day": list_day,
                "List_time": list_time
            })
        
    return Response(data=result)

           

