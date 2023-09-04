from django import forms
from django.forms import ModelForm
from .models import Job

# Job form
class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'description')
        

