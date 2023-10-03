from django import forms
from django.forms import ModelForm
from .models import Job, CoverLetter, Source, ReferenceProject

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ('company', 'position', 'description', 'URL')
        widgets = {
            'date_posted': forms.DateInput(attrs={'type': 'date'}),
            'date_apply': forms.DateInput(attrs={'type': 'date'})
        }
        
class CLForm(ModelForm):
    class Meta:
        model = CoverLetter
        fields = ('questionnaire_looking_for', 'questionnaire_relevant_experience', 'questionnaire_relevant_work_links', 'questionnaire_how_solve', 'questionnaire_portfolio_links')

class CLForm_Text(ModelForm):
    class Meta:
        model = CoverLetter
        fields = ('text',)

class CLForm_Main(ModelForm):
    class Meta:
        model = CoverLetter
        fields = ('main_self_name', 'main_self_address', 'main_subject', 'main_cover_letter_date')
        widgets = {
            'main_cover_letter_date': forms.DateInput(attrs={'type': 'date'}),
        }

class JobForm_ReferenceNotes(ModelForm):
    class Meta:
        model = Job
        fields = ('reference_notes',)

class SourceForm(ModelForm):
    class Meta:
        model = Source
        fields = ('name', 'link')

class JobCaseSelectionForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['case_select'] = forms.ModelChoiceField(
            queryset=Job.objects.filter(user=user).order_by('-id'),
            empty_label="Job"
        )
    
class JobForm_Company(ModelForm):
    class Meta:
        model = Job
        fields = ('company', 'address')

class ReferenceProjectForm(ModelForm):
    class Meta:
        model = ReferenceProject
        fields = ('reference_title', 'reference_about', 'reference_date', 'reference_company', 'reference_description', 'reference_problem_statement', 'reference_to_whom_solve', 'reference_bottleneck_solve', 'reference_time_taken', 'reference_solution', 'reference_results', 'reference_testimonials', 'reference_visuals', 'reference_skills', 'reference_links')
        widgets = {
            'reference_date': forms.DateInput(attrs={'type': 'date'}),
        }