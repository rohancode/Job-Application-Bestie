from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.user.username

class Job(models.Model):
    position = models.CharField(default='', max_length=255, null=True, blank=True)
    description = models.TextField(default='', null=True, blank=True)
    cover_letter_done = models.BooleanField(default=False, null=True, blank=True)
    resume_done = models.BooleanField(default=False, null=True, blank=True)
    proofreading_done = models.BooleanField(default=False, null=True, blank=True)
    application_sent_done = models.BooleanField(default=False, null=True, blank=True)
    contact_person = models.CharField(default='', max_length=255, null=True, blank=True)
    URL = models.CharField(default='', max_length=255, null=True, blank=True)
    extracted_key_words = models.TextField(default='', null=True, blank=True)
    address = models.TextField(default='', null=True, blank=True)
    reference_notes = models.TextField(default='', null=True, blank=True)
    date_posted = models.DateField(default=timezone.now, null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    company = models.CharField(default='', max_length=255, null=True, blank=True)
    date_apply = models.DateField(default=timezone.now, null=True, blank=True)
    interview_call = models.BooleanField(default=False, null=True, blank=True)
    interview_call_date = models.DateField(default=timezone.now, null=True, blank=True)
    eligible_pre_check_good_idea = models.BooleanField(default=False, null=True, blank=True)
    eligible_pre_check_status = models.BooleanField(default=False, null=True, blank=True)
    priority_choices = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    priority = models.CharField(default='medium', max_length=10, choices=priority_choices, null=True, blank=True)
    acceptance_chance_choices = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    acceptance_chance_feeling = models.CharField(default='medium', max_length=10, choices=acceptance_chance_choices, null=True, blank=True)
    documents_prep_time_choices = [
        ('high', 'High'),
        ('normal', 'Normal'),
        ('low', 'Low'),
    ]
    documents_prep_time_feeling = models.CharField(default='medium', max_length=10, choices=documents_prep_time_choices, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_user', null=True)

    def __str__(self):
        return f'{self.id} - {self.company} - {self.position}'

class CoverLetter(models.Model):
    questionnaire_self_introduction = models.TextField(default='', null=True, blank=True)
    questionnaire_looking_for = models.TextField(default='', null=True, blank=True)
    questionnaire_relevant_experience = models.TextField(default='', null=True, blank=True)
    questionnaire_relevant_work_links = models.TextField(default='', null=True, blank=True)
    questionnaire_how_solve = models.TextField(default='', null=True, blank=True)
    questionnaire_personality_strengths = models.TextField(default='', null=True, blank=True)
    questionnaire_portfolio_links = models.TextField(default='', null=True, blank=True)
    main_self_name = models.CharField(default='', max_length=255, null=True, blank=True)
    main_self_address = models.TextField(default='', null=True, blank=True)
    main_subject = models.CharField(default='', max_length=255, null=True, blank=True)
    main_cover_letter_date = models.DateField(default=timezone.now, null=True, blank=True)
    text = models.TextField(default='', null=True, blank=True)
    type_choices = [
        ('reply_pos', 'Reply_Pos'),
        ('reply_neg', 'No_Reply'),
        ('neutral', 'Neutral'),
    ]
    reference_type = models.CharField(default='neutral', max_length=10, choices=type_choices, null=True, blank=True)
    job = models.OneToOneField(Job, on_delete=models.CASCADE, related_name='cover_letters_job', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cover_letters_user', null=True)

    def __str__(self):
        return self.text

class ReferenceProject(models.Model):
    reference_title = models.CharField(default='', max_length=255, null=True, blank=True)
    reference_about = models.TextField(default='', null=True, blank=True)
    reference_date = models.DateField(default=timezone.now, null=True, blank=True)
    reference_company = models.CharField(default='', max_length=255, null=True, blank=True)
    reference_description = models.TextField(default='', max_length=255, null=True, blank=True)
    reference_problem_statement = models.TextField(default='', max_length=255, null=True, blank=True)
    reference_to_whom_solve = models.TextField(default='', max_length=255, null=True, blank=True)
    reference_bottleneck_solve = models.TextField(default='', max_length=255, null=True, blank=True)
    reference_time_taken = models.TextField(default='', max_length=255, null=True, blank=True)
    reference_solution = models.TextField(default='', max_length=255, null=True, blank=True)
    reference_results = models.TextField(default='', max_length=255, null=True, blank=True)
    reference_testimonials = models.TextField(default='', max_length=255, null=True, blank=True)
    reference_visuals = models.TextField(default='', max_length=255, null=True, blank=True)
    reference_skills = models.TextField(default='', max_length=255, null=True, blank=True)
    reference_links = models.TextField(default='', max_length=255, null=True, blank=True)
    reference_to_portfolio = models.BooleanField(default=True, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reference_project_user', null=True)

    def __str__(self):
        return self.reference_title

class Source(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='source_user', null=True)

    def __str__(self):
        return self.name

class UserConsent(models.Model):
    user_ip = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)
    essential_cookies = models.BooleanField(default=False)