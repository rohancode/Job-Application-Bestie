from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.user.username

class Job(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs', null=True)

    def __str__(self):
        return self.title

class CoverLetter(models.Model):
    text = models.TextField(null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='cover_letters', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cover_letters', null=True)

    def __str__(self):
        return f"Cover Letter for {self.job.title} by {self.user.username}"


# class CoverLetter(models.Model):
#     content = models.TextField(blank=True)

#     def __str__(self):
#         return self.content

# class Member(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)

#     def __str__(self):
#         return self.first_name + ' ' + self.last_name

# class Job(models.Model):
#     title = models.CharField('Job Title', max_length=120)
#     description = models.TextField(blank=True)
#     link = models.URLField('Link')
#     contact = models.CharField('Contact', max_length=120)
#     industry = models.ForeignKey(CoverLetter, blank=True, null=True, on_delete=models.CASCADE)
#     applicants = models.ManyToManyField(Member, blank=True)

#     def __str__(self):
#         return self.title