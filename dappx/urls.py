# dappx/urls.py
from django.conf.urls import url
from dappx import views
from dprojx import settings
# SET THE NAMESPACE!
app_name = 'dappx'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^offerdetails/$',views.register,name='offerdetails'),
    ]
