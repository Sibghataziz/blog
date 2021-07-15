from django import forms
from .models import Post,Comment

class Add_Post(forms.Form):
    body = forms.CharField(max_length=2000)

class Add_Comment(forms.Form):
    body = forms.CharField(max_length=200)

