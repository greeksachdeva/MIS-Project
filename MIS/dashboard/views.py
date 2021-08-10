from django.contrib.auth.models import User
from dashboard.models import rolesall
from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount, SocialApp
# Create your views here.
from django.http import HttpResponse


"""role checker"""
def roles_required(roles):
    def inner_func(f):
        """ Decorator to check if the user is not authorized."""

        def wrap(request, *args, **kwargs):
            email = request.user.email
            match = rolesall.objects.get(email=email)
            user_role = match.roles
            if user_role not in roles:
                return HttpResponse("<h1>User not authorized to access this :D ")
            return f(request, *args, **kwargs)

        wrap.__doc__ = f.__doc__
        wrap.__name__ = f.__name__
        return wrap

    return inner_func

#@roles_required(roles=[1]) # for functions that you want teacher to access,
#@roles_required(roles=[0]) # for functions that you want student to access
def check_email(request):
    if not request.user.is_authenticated:
        return HttpResponse("<h1>NOT AUTHENTICATED")
    """ Decorator to check if the user is not authorized."""
    """ check if email in db"""

    # Get the email
    email = request.user.email

    # Check to see if any users already exist with this email as a username.
    try:
        match = rolesall.objects.get(email=email)
        print(match)
        roles = match.roles
        if roles == 0:
            return HttpResponse("<h1>HELLO STUDENT")
        elif roles == 1:
            return HttpResponse("<h1>HELLO TEACHER")

            # print(dir(match))

        """ redirect"""
    except rolesall.DoesNotExist:
        # Unable to find a user, this is fine
        return HttpResponse("<h1>not in database")
        # return create_response(code=constants.FORBIDDEN,
        #                      message="You have insufficient permissions for this task")




#def index(request):
 #   if not request.user.is_authenticated:
  #      return HttpResponse("<h1>not authenticated")

   # print(dir(request.user))
    #print(request.user.email)

    #return HttpResponse("<h1>Hello world")
