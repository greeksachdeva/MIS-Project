from django.urls import path, include


from . import views

app_name='misapp'

urlpatterns = [
    path('', views.signup, name='signup_ap'),
    path('',views.login,name='login_ap'),
]