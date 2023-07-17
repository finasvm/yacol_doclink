from django import forms
from .models import *

class Result_form(forms.ModelForm):
    class Meta:
        model=Results
        fields  = ['filename', 'file','user']
        labels={
            'filename':'name',
             'choose_file':'file',
             'select_user':'user'
        }
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
             'choose_file':forms.ClearableFileInput(attrs={'class':'form-control'}),
             'select_user':forms.TextInput(attrs={'class':'form-control'})

           
        }