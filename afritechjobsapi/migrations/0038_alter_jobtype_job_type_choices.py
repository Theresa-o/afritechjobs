# Generated by Django 5.0.6 on 2024-07-16 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afritechjobsapi', '0037_remove_postajob_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobtype',
            name='job_type_choices',
            field=models.CharField(choices=[('Contract', 'Contract'), ('FullTime', 'FullTime'), ('Freelance', 'Freelance'), ('Internship', 'Internship'), ('Parttime', 'Parttime')], default='FullTime', max_length=15),
        ),
    ]