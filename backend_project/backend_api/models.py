from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    start_time=models.CharField(max_length=25,null=True,blank=True)
    end_time=models.CharField(max_length=25,null=True,blank=True)
    image=models.ImageField(upload_to='doc_image',null=True,blank=True)

    def __str__(self):
        return self.name   
    
class Days(models.Model):
    sunday=models.BooleanField(default=False,null=True,blank=True)
    monday=models.BooleanField(default=False,null=True,blank=True)
    tuesday=models.BooleanField(default=False,null=True,blank=True)
    wednesday=models.BooleanField(default=False,null=True,blank=True)
    thursday=models.BooleanField(default=False,null=True,blank=True)
    friday=models.BooleanField(default=False,null=True,blank=True)
    saturday=models.BooleanField(default=False,null=True,blank=True)
    doc_link=models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='docdays')


class Appointment(models.Model):
    fullname=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    civilid=models.CharField(max_length=100,null=True,blank=True)
    gender=models.CharField(max_length=20)
    age=models.CharField(max_length=20)
    disease=models.CharField(max_length=500)
    sch_date=models.CharField(max_length=50)
    sch_time=models.CharField(max_length=50)
    user_cus=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    doc=models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='doctor')
    status=models.CharField(max_length=50,default='ongoing',null=True,blank=True)

class Results(models.Model):
    filename=models.CharField(max_length=100)
    file=models.FileField(upload_to='result_files',null=True,blank=True)
    description=models.CharField(max_length=200,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='res_user')