from django import forms
from django.forms import ModelForm
from .models import Job, CoverLetter

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'description')
        
class CLForm(ModelForm):
    class Meta:
        model = CoverLetter
        fields = ('text',)