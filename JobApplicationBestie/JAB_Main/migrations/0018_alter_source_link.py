# Generated by Django 4.2.4 on 2023-10-02 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JAB_Main', '0017_coverletter_main_cover_letter_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
