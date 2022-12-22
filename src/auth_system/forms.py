from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import *

class CreateNewUser(UserCreationForm):
    class Meta:
        model = User 
        fields =['email','first_name','last_name','password1','password2','username']
        error_messages = {
            'password1': {
                'required': ('Please enter a password.')
            },
            'password2': {
                'required': ('Please enter a password.')
            }}
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'first_name'}),
            'email': forms.TextInput(attrs={'placeholder': 'email'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'last_name'}),
            'password1': forms.TextInput(attrs={'placeholder': 'password'}),
            'password2': forms.TextInput(attrs={'placeholder': 'confirm password'}),
            'username': forms.TextInput(attrs={'placeholder': 'username'}),
            
        }

class EditeUserInfoForm(forms.ModelForm):
    class Meta:
        model = User 
        fields =['email','first_name','last_name']
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'email'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'last_name'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'first_name'}),
            
        }



    
class EditeProfileInfoForm(forms.ModelForm):
    class Meta:
        model = Add
        fields =['img','phone','are_you_doctor']
        widgets = {
            
            'phone': forms.TextInput(attrs={'placeholder': 'phone '}),
            # 'are_you_doctor': forms.TextInput(attrs={'placeholder': 'are_you_doctor'}),
            
        }





class AddsForm(ModelForm):
    # def create (un,self):
    #     self.user = un
    class Meta:
        model = Add
        fields = ['address','price','weatingHours','workingHours']
        widgets = {
            'address': forms.TextInput(attrs={'placeholder': 'address'}),
            'price': forms.TextInput(attrs={'placeholder': 'price'}),
            'weatingHours': forms.TextInput(attrs={'placeholder': 'weatingHours'}),
            'workingHours': forms.TextInput(attrs={'placeholder': 'workingHours'}),
            
        }

    
