# Generated by Django 4.2.1 on 2023-06-07 11:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('afritechjobsapi', '0012_joblocations_postajob_job_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobskills',
            name='user',
        ),
        migrations.AddField(
            model_name='postajob',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postajob',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
