# Generated by Django 4.2.1 on 2023-06-02 06:54

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('afritechjobsapi', '0005_alter_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image',
        ),
    ]
