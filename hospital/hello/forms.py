from django.core import validators
from django import forms
from .models import Medicine
from .models import Nurse



# Field name made lowercase.


class Add_Medicine(forms.ModelForm):
    class Meta:
     model=Medicine
     fields= ['medicine_id', 'medicine_name', 'patient_id', 'expired_date', 'price']
     widgets= {
         'medicine_id': forms.TextInput(attrs={'class':'form-control'}),
         'medicine_name': forms.TextInput(attrs={'class':'form-control'}),
         'patient_id': forms.TextInput(attrs={'class':'form-control'}),
         'expired_date': forms.DateInput(attrs={'class':'form-control'}),
         'price': forms.TextInput(attrs={'class':'form-control'}),
     }

class Add_Nurse(forms.ModelForm):
    class Meta:
     model=Nurse
     fields= ['nurse_id', 'nurse_name', 'floor_no']
     widgets= {
         'nurse_id': forms.TextInput(attrs={'class':'form-control'}),
         'nurse_name': forms.TextInput(attrs={'class':'form-control'}),
         'floor_no': forms.TextInput(attrs={'class':'form-control'}),
        
     }



