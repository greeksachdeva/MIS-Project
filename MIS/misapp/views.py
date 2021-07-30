from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib import messages
from django.core.mail import send_mail
import random
# Create your views here.
def login(request):
    if request.session.has_key('uid'):
        context = {'username': request.session['uid']}
        return render(request, 'misapp/services.html', context)
    if request.method == 'POST':
        curr_user = misapp.objects.all().filter(
            pk=request.POST["username"], password=request.POST["password"])
        if curr_user.count() == 1:
            request.session['uid'] = request.POST["username"]
            context = {'username': request.session['uid']}
            return render(request, 'misapp/services.html', context)
        else:
            messages.info(request, "Invalid Username/Password")
    context = {}
    return render(request, 'misapp/login.html', context)