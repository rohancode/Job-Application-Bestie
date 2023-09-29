from django import forms
from django.forms import ModelForm
from .models import Job, CoverLetter, Source

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ('company', 'position', 'description', 'contact_person', 'URL', 'address', 'date_posted', 'date_apply', 'eligible_pre_check_good_idea', 'priority', 'acceptance_chance_feeling', 'documents_prep_time_feeling')
        widgets = {
            'date_posted': forms.DateInput(attrs={'type': 'date'}),
            'date_apply': forms.DateInput(attrs={'type': 'date'}),
        }
        
class CLForm(ModelForm):
    class Meta:
        model = CoverLetter
        fields = ('text',)

class SourceForm(ModelForm):
    class Meta:
        model = Source
        fields = ('name', 'link')