from django import forms
from vehicle.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class contactform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=contact
        
class servicesform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=services


class signupform( UserCreationForm):
        class Meta:
         fields=('first_name','last_name','username','email','password1','password2')
         model=User

class appointmentform(forms.ModelForm):
    class Meta:
        fields='__all__'
        model=appointment
        

         




