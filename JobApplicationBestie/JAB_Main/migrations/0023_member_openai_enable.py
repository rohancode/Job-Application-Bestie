# Generated by Django 4.2.4 on 2023-10-07 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JAB_Main', '0022_member_openai_api_alter_member_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='openai_enable',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
