# Generated by Django 4.2.1 on 2023-06-01 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afritechjobsapi', '0003_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
    ]