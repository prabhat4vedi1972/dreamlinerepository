# dappx/forms.py
from django import forms
from dappx.models import Person
from django.contrib.auth.models import User

class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = Person
         fields = ('name','email','phone','city','query')
         required_css_class = 'bold'