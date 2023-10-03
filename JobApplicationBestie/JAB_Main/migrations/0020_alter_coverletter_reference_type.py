# Generated by Django 4.2.4 on 2023-10-03 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JAB_Main', '0019_rename_comments_job_reference_notes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coverletter',
            name='reference_type',
            field=models.CharField(blank=True, choices=[('reply_pos', 'Reply_Pos'), ('reply_neg', 'No_Reply'), ('neutral', 'Neutral')], default='neutral', max_length=10, null=True),
        ),
    ]
