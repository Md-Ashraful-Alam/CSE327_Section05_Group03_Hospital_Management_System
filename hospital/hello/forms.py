from django.core import validators
from django import forms
from .models import Bed
from .models import BloodDonate



# Field name made lowercase.



class Add_Bed(forms.ModelForm):
    class Meta:
     model=Bed
     fields= ['bed_id', 'bed_type', 'vacancy', 'bed_charge']
     widgets= {
         'appointment_id': forms.TextInput(attrs={'class':'form-control'}),
         'bed_type': forms.TextInput(attrs={'class':'form-control'}),
         'vacancy': forms.TextInput(attrs={'class':'form-control'}),
         'bed_charge': forms.TextInput(attrs={'class':'form-control'}),
      
     }
  

 

class Add_BloodDonate(forms.ModelForm):
    class Meta:
     model=BloodDonate
     fields= ['patient_id', 'user_id', 'blood_group', 'contact_num','location','need_date']
     widgets= {
         'patient_id': forms.TextInput(attrs={'class':'form-control'}),
         'user_id': forms.TextInput(attrs={'class':'form-control'}),
         'blood_group': forms.TextInput(attrs={'class':'form-control'}),
         'contact_num': forms.TextInput(attrs={'class':'form-control'}),
         'location': forms.TextInput(attrs={'class':'form-control'}),
         'need_date': forms.DateInput(attrs={'class':'form-control'}),
      
     } 


