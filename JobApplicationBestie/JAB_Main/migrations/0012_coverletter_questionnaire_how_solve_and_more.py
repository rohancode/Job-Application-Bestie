# Generated by Django 4.2.4 on 2023-09-30 18:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('JAB_Main', '0011_alter_coverletter_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='coverletter',
            name='questionnaire_how_solve',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='coverletter',
            name='questionnaire_looking_for',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='coverletter',
            name='questionnaire_personality_strengths',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='coverletter',
            name='questionnaire_portfolio_links',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='coverletter',
            name='questionnaire_relevant_experience',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='coverletter',
            name='questionnaire_relevant_work_links',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='coverletter',
            name='questionnaire_self_introduction',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='URL',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='acceptance_chance_feeling',
            field=models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], default='medium', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='address',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='comments',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='contact_person',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='date_apply',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='date_posted',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='documents_prep_time_feeling',
            field=models.CharField(choices=[('high', 'High'), ('normal', 'Normal'), ('low', 'Low')], default='medium', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='extracted_key_words',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='interview_call_date',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='position',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='priority',
            field=models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], default='medium', max_length=10, null=True),
        ),
    ]