from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('accounts/LogIn/', GeneralLogin, name='signin'),
   
   
]