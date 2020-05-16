from django.forms import ModelForm
from django import forms

from .models import *

class PostForm(ModelForm):
    class Meta:
        model = Post
        filter = '__all__'
        exclude = ['user']