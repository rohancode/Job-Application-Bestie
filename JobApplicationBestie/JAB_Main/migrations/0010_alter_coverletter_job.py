# Generated by Django 4.2.4 on 2023-09-30 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('JAB_Main', '0009_alter_job_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coverletter',
            name='job',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cover_letters_job', to='JAB_Main.job'),
        ),
    ]
