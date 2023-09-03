from django.db import models

class CoverLetter(models.Model):
    content = models.TextField(blank=True)

    def __str__(self):
        return self.content

class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Job(models.Model):
    title = models.CharField('Job Title', max_length=120)
    description = models.TextField(blank=True)
    link = models.URLField('Link')
    contact = models.CharField('Contact', max_length=120)
    industry = models.ForeignKey(CoverLetter, blank=True, null=True, on_delete=models.CASCADE)
    applicants = models.ManyToManyField(Member, blank=True)

    def __str__(self):
        return self.title


