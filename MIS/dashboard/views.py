from django.contrib.auth.models import User
from dashboard.models import rolesall
from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount, SocialApp

# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view


def check_email(request):

        if not request.user.is_authenticated:
            return HttpResponse("<h1>not authenticated")
        """ Decorator to check if the user is not authorized."""
        """ check if email in db"""

        # Get the email
        email = request.user.email

        # Check to see if any users already exist with this email as a username.
        try:
            match = rolesall.objects.get(email=email)
            print(match)
            roles = match.roles
            if roles==0:
                return HttpResponse("welcome Student")
            elif roles==1:
                return HttpResponse("welcome teacher")    

            #print(dir(match))
            
            
            """ redirect"""
        except rolesall.DoesNotExist:
            # Unable to find a user, this is fine
            return HttpResponse("not in database")
            # return create_response(code=constants.FORBIDDEN,
            #                      message="You have insufficient permissions for this task")


"""role checker"""


#def index(request):
 #   if not request.user.is_authenticated:
  #      return HttpResponse("<h1>not authenticated")

   # print(dir(request.user))
    #print(request.user.email)

    #return HttpResponse("<h1>Hello world")
