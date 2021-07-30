from django.db import models

# Create your models here.
class misapp(models.Model):
    username=models.EmailField(unique=True)
    password=models.CharField(max_length=20)