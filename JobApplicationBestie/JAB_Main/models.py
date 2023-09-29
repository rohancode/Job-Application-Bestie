from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.user.username

class Job(models.Model):
    position = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    cover_letter_done = models.BooleanField(default=False, null=True)
    resume_done = models.BooleanField(default=False, null=True)
    proofreading_done = models.BooleanField(default=False, null=True)
    application_sent_done = models.BooleanField(default=False, null=True)
    contact_person = models.CharField(max_length=255, null=True)
    URL = models.CharField(max_length=255, null=True)
    extracted_key_words = models.TextField(null=True)
    address = models.TextField(null=True)
    comments = models.TextField(null=True)
    date_posted = models.DateField(null=True)
    date_add = models.DateTimeField(auto_now_add=True, null=True)
    company = models.CharField(max_length=255, null=True)
    date_apply = models.DateField(null=True)
    interview_call = models.BooleanField(default=False, null=True)
    interview_call_date = models.DateField(null=True)
    eligible_pre_check_good_idea = models.BooleanField(default=False, null=True)
    eligible_pre_check_status = models.BooleanField(default=False, null=True)
    priority_choices = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    priority = models.CharField(max_length=10, choices=priority_choices, null=True)
    acceptance_chance_choices = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    acceptance_chance_feeling = models.CharField(max_length=10, choices=acceptance_chance_choices, null=True)
    documents_prep_time_choices = [
        ('high', 'High'),
        ('normal', 'Normal'),
        ('low', 'Low'),
    ]
    documents_prep_time_feeling = models.CharField(max_length=10, choices=documents_prep_time_choices, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_user', null=True)

    def __str__(self):
        return self.position

class CoverLetter(models.Model):
    text = models.TextField(null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='cover_letters_job', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cover_letters_user', null=True)

    def __str__(self):
        return self.text

class Source(models.Model):
    name = models.CharField(max_length=255, null=True)
    link = models.URLField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='source_user', null=True)

    def __str__(self):
        return self.name