from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *

class UserForm(UserCreationForm):
    Gender = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    full_name = forms.CharField(max_length=100)
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    email = forms.CharField(max_length=100, help_text='email')
    gender = forms.ChoiceField(choices=Gender)

    class Meta:
        model = User
        fields = ('username','password1','password2','email','full_name','birth_date','gender')



