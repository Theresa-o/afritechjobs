# Generated by Django 4.2.1 on 2023-06-02 07:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('afritechjobsapi', '0006_remove_blog_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
    ]
