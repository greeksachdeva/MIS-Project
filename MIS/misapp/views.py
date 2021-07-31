from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login
import random
# Create your views here.
def signup_ap(request):
    if request.method =='POST' :
        form=UserCreationForm(request.POST)
        if(form.is_valid()):
            #creating user
            user=form.save()
            login(request,user)
            #login
            return redirect('misapp:home')
    else:
        form=UserCreationForm()
    return render(request, 'misapp/signup.html',{'form':form})
def login_ap(request):
    if request.method=='POST':
        #check validation and log in
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log the user in
            user=form.get_user()
            login(request,user)
            return redirect('misapp:home')
    else:
        #GET req-click on login
        form=AuthenticationForm()
    #throw error
    return render(request,'misapp/login.html',{'form':form})
