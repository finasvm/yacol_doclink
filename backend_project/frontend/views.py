from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView
from django.contrib import messages
from django.http import HttpResponse,JsonResponse 
from backend_api.models import *
from backend_api.forms import Result_form
from django.urls import reverse_lazy

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
        appointments=Appointment.objects.all()
        return render(request,'appointments.html',{'appointments':appointments})
    
class OrderChange(View):
    def post(self,request):
        values =request.POST['Value']
        id1 = request.POST['id1']
        print('//////////')
        appoint = Appointment.objects.get(id=id1)
        if values =='Approved':
            print('////////////')
            appoint.status = 'Approved'
        else:
            appoint.status = 'Declined'
        appoint.save()
        return JsonResponse('true',safe=False)
    
class Reports(View):
    def get(self,request):
        report=Appointment.objects.all()
        return render(request,'reports.html',{'report':report})
    
class All_Results(View):
    def get(self,request):
        result=Results.objects.all()
        return render(request,'results.html',{'result':result})
    
class SendResult(CreateView):
    model=Results
    form_class=Result_form
    template_name='sendresult.html'
    success_url=reverse_lazy('results')

    def form_valid(self, form):
            form.instance.user=self.request.user
            self.object = form.save()
            messages.success(self.request,'Results added successfully')
            return super().form_valid(form)




            