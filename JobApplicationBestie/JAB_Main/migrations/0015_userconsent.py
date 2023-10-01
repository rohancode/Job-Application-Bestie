# Generated by Django 4.2.4 on 2023-10-01 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JAB_Main', '0014_alter_coverletter_main_self_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserConsent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ip', models.GenericIPAddressField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('essential_cookies', models.BooleanField(default=False)),
            ],
        ),
    ]
