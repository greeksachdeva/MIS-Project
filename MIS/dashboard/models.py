from django.contrib.auth.models import User
from django.db import models

class rolesall(models.Model):
    MY_CHOICES = (
        ('0', 'Student'),
        ('1', 'Teacher'),
    )
    first_name = models.CharField(max_length=30)
    email = models.EmailField( max_length=100,unique=True, primary_key = True)
    roles=models.IntegerField(max_length=1)