# dappx/views.py
from django.shortcuts import render
from dappx.forms import UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage

def index(request):
    return render(request,'dappx/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered = False
    if request.method == 'POST':
        #user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if profile_form.is_valid():
#            user = user_form.save()
#            user.set_password(user.password)
 #           user.save()
            profile = profile_form.save(commit=False)
            customer_name=profile_form.cleaned_data['name']
            customer_phone=profile_form.cleaned_data['phone']
            email = EmailMessage('New Registration: '+customer_name, customer_name+' is interested in the tour package. Please call him on '+customer_phone+' to discuss further.', to=['prabhat4vedi@gmail.com'])
            email.send()
            print(customer_name,customer_phone)
            from twilio.rest import Client
            from django.conf import settings

            to = '+918169813384'
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            response = client.messages.create(body='New Registration: '+customer_name+'. '+customer_name+' is interested in the tour package. Please call him on '+customer_phone+' to discuss further.', 
                 to=to, from_=settings.TWILIO_PHONE_NUMBER)
  #S          profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(profile_form.errors)
    else:
        profile_form = UserProfileInfoForm()
    return render(request,'dappx/registration.html',
                          {'profile_form':profile_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'dappx/login.html', {})