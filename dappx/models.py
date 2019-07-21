# dappx/models.py
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
# class UserProfileInfo(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     portfolio_site = models.URLField(blank=True)
#     profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
#     content = models.TextField(max_length=300)
# def __str__(self):
#   return self.user.username
class Person(models.Model):
    name = models.CharField(max_length=96)
    email= models.EmailField(max_length=254, blank=False, unique=True,
        error_messages={'required': 'Please provide your email address.',
                        'unique': 'An account with this email exist.'},)
    phone =  models.CharField(max_length=10)
    city = models.CharField(max_length=96)
    date_registered = models.TimeField
    query = models.TextField(max_length=300,default='I am interested. Please call on XXXXXXXXXX', editable=True)
    
# from django.forms import ModelForm

# class SubscribeForm(ModelForm):
#     class Meta:
#         model = Person
#         exclude = ('date_subscribed','messages_received')