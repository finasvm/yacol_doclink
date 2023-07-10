from django.db import models

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
