from django.core import validators
from django import forms
from .models import OrganDonate
from .models import User


# Field name made lowercase.

 

class Add_OrganDonate(forms.ModelForm):
    class Meta:
     model=OrganDonate

     fields= ['patient_id', 'user_id', 'blood_group', 'contact_num','location','need_date']
     widgets= {
         'patient_id': forms.TextInput(attrs={'class':'form-control'}),
         'user_id': forms.TextInput(attrs={'class':'form-control'}),
         'blood_group': forms.TextInput(attrs={'class':'form-control'}),
         'contact_num': forms.TextInput(attrs={'class':'form-control'}),
         'location': forms.TextInput(attrs={'class':'form-control'}),
         'need_date': forms.DateInput(attrs={'class':'form-control'}),   
     } 





class Add_User(forms.ModelForm):
    class Meta:
     model=User
     fields= ['user_id', 'user_name', 'address', 'blood_group','age', 'email', 'user_type']
     widgets= {
         'user_id': forms.TextInput(attrs={'class':'form-control'}),
         'user_name': forms.TextInput(attrs={'class':'form-control'}),
         'address': forms.TextInput(attrs={'class':'form-control'}),
         'blood_group': forms.TextInput(attrs={'class':'form-control'}),
         'age': forms.TextInput(attrs={'class':'form-control'}),
         'email': forms.TextInput(attrs={'class':'form-control'}),
         'user_type': forms.TextInput(attrs={'class':'form-control'}),
     }