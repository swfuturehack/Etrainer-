from django.urls import path
from .views import *

app_name = 'teacher'

urlpatterns = [
    path('teachersignup/', signup, name='teacher-signup'),
    path('dashboard/', cpanel, name='dashboard'),
    path('course/', course, name='course'),   
]