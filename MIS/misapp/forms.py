from django import forms
from .models import *

class misappforms(forms.ModelForm):

    class Meta:
        model = misapp
        fields = "__all__"