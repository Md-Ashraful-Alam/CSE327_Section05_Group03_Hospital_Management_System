from django.core import validators
from django import forms
from .models import Appointment
from .models import Test
from .models import Doctor


# Field name made lowercase.

class Add_Appointment(forms.ModelForm):
    class Meta:
     model=Appointment
     fields= ['appointment_id', 'patient_id', 'doctor_id', 'appointment_date']
     widgets= {
         'appointment_id': forms.TextInput(attrs={'class':'form-control'}),
         'patient_id': forms.TextInput(attrs={'class':'form-control'}),
         'doctor_id': forms.TextInput(attrs={'class':'form-control'}),
         'appointment_date': forms.DateInput(attrs={'class':'form-control'}),
      
     }




class Add_Doctor(forms.ModelForm):
    class Meta:
     model=Doctor
     fields= ['doctorid', 'user_id', 'doctor_name', 'contact_num', 'email', 'meet_link']
     widgets= {
         'doctorid': forms.TextInput(attrs={'class':'form-control'}),
         'user_id': forms.TextInput(attrs={'class':'form-control'}),
         'doctor_name': forms.TextInput(attrs={'class':'form-control'}),
         'contact_num': forms.TextInput(attrs={'class':'form-control'}),
         'email': forms.TextInput(attrs={'class':'form-control'}),
         'meet_link': forms.TextInput(attrs={'class':'form-control'}),
     }


class Add_Test(forms.ModelForm):
    class Meta:
     model=Test
     fields= ['test_id', 'patient_id', 'test_charge']
     widgets= {
         'test_id': forms.TextInput(attrs={'class':'form-control'}),
         'patient_id': forms.TextInput(attrs={'class':'form-control'}),
         'test_charge': forms.TextInput(attrs={'class':'form-control'}),
        
     }






