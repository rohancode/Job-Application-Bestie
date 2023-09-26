from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.user.username

class Job(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='job_user', null=True)

    def __str__(self):
        return self.title

class CoverLetter(models.Model):
    text = models.TextField(null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='cover_letters_job', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cover_letters_user', null=True)

    def __str__(self):
        return self.text

