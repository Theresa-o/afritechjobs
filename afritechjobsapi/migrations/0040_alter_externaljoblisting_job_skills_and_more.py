# Generated by Django 5.0.6 on 2024-08-14 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afritechjobsapi', '0039_alter_joblevel_job_level_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='externaljoblisting',
            name='job_skills',
            field=models.ManyToManyField(blank=True, to='afritechjobsapi.jobskills'),
        ),
        migrations.AlterField(
            model_name='hiringguide',
            name='category',
            field=models.ManyToManyField(blank=True, to='afritechjobsapi.category'),
        ),
        migrations.AlterField(
            model_name='postajob',
            name='job_skills',
            field=models.ManyToManyField(blank=True, to='afritechjobsapi.jobskills'),
        ),
        migrations.AlterField(
            model_name='workresources',
            name='category',
            field=models.ManyToManyField(blank=True, to='afritechjobsapi.category'),
        ),
    ]
