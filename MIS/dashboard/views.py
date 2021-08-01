from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
@login_required(login_url ="login")

def index(request):
    return HttpResponse("<h1>This is home page")

# Create your views here.
