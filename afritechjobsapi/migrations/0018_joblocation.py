# Generated by Django 4.2.1 on 2023-06-09 11:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('afritechjobsapi', '0017_rename_joblocation_joblocations'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
