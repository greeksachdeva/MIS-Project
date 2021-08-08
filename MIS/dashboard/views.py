from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount, SocialApp

# Create your views here.
from django.http import HttpResponse


def index(request):
    if not request.user.is_authenticated:
        return HttpResponse("<h1>not authenticated")

    print(dir(request.user))
    print(request.user.email)

    return HttpResponse("<h1>Hello world")
