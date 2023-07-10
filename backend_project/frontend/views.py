from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from django.contrib import messages

# Create your views here.

class Login(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
            username = request.POST.get('username')
            password = request.POST.get('password')
            if (username =="finasvm" and password =="1234"):
                request.session['key'] = 'user'
                return redirect('appoint')
            messages.success(request,'username and password is wrong')
            return redirect('login')

class Appointments(View):
    def get(self,request):
        return render(request,'appointments.html')
    
class Reports(View):
    def get(self,request):
        return render(request,'reports.html')