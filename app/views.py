from django.shortcuts import render
from django.views.generic import *
from teacher.models import *
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
import datetime

# Create your views here.


class Index(TemplateView):
	template_name = 'index.html'





def GeneralLogin(request):
    template_name = 'registration/login.html'
    logout(request)
    username = password = ''

    #myDate = datetime.datetime.now()

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('teacher:dashboard')
        
		
    return render(request, template_name)
