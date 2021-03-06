from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Register_form(UserCreationForm):
    email = forms.EmailField()
    First_Name = forms.CharField(max_length=32)
    Last_Name = forms.CharField(max_length=32)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('First_Name','Last_Name','email')
    