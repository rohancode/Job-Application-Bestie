# Generated by Django 4.2.4 on 2023-10-20 23:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('JAB_Main', '0026_alter_questionnairecustom_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnairecustom',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire_custom_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
