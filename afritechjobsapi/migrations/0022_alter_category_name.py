# Generated by Django 4.2.1 on 2023-06-09 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afritechjobsapi', '0021_joblocations_alter_postajob_job_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
