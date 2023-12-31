# Generated by Django 4.2.4 on 2023-09-29 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JAB_Main', '0006_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='URL',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='acceptance_chance_feeling',
            field=models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='application_sent_done',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='comments',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='company',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='contact_person',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='cover_letter_done',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='date_apply',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='date_posted',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='documents_prep_time_feeling',
            field=models.CharField(choices=[('high', 'High'), ('normal', 'Normal'), ('low', 'Low')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='eligible_pre_check_good_idea',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='eligible_pre_check_status',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='extracted_key_words',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='interview_call',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='interview_call_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='priority',
            field=models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='proofreading_done',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='resume_done',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
