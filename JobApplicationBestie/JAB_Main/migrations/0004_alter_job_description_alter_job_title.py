# Generated by Django 4.2.4 on 2023-09-04 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JAB_Main', '0003_remove_coverletter_content_remove_job_applicants_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
