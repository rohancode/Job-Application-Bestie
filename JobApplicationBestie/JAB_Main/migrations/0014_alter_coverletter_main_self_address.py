# Generated by Django 4.2.4 on 2023-09-30 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JAB_Main', '0013_coverletter_main_self_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coverletter',
            name='main_self_address',
            field=models.TextField(default='', null=True),
        ),
    ]
