from django.forms import ModelForm
from django import forms
from .models import Cake

class PostCake(ModelForm):
    class Meta:
        model = Cake
        fields = '__all__'
        exclude = ['cake_info']