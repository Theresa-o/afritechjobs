# Generated by Django 4.2.1 on 2023-06-15 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('afritechjobsapi', '0026_alter_joblevel_job_level_choices_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='postajob',
            name='created_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='afritechjobsapi.profile'),
        ),
    ]
