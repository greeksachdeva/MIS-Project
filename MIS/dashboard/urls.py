from django.urls import path
from . import views
urlpatterns = [
    path('',views.check_email,name = 'check_email'),
    #path('',views.roles_required,name='roles_required'),
]