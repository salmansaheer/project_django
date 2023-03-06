from django import forms
from .models import *

class USERS(forms.ModelForm):
    class Meta:
        model = Users
        exclude = ['general_details']
        widgets = {
            'marital': forms.Select(),
            'gender': forms.Select(),
            'bloodgroup':forms.Select(),
            'dob':forms.DateInput(),
        }

class GENERALDETAILS(forms.ModelForm):
    class Meta:
        model =GeneralDetails
        exclude = ['role']
        widgets = {
        }
        

class HOSPITAL(forms.ModelForm):
    class Meta:
        model = Hospital
        exclude = ['general_details','role']
        widgets = {
            'brand': forms.Select()
        }