# Generated by Django 4.2.1 on 2023-06-06 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('afritechjobsapi', '0011_remove_postajob_job_location_delete_joblocation'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobLocations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='postajob',
            name='job_location',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='afritechjobsapi.joblocations'),
        ),
    ]