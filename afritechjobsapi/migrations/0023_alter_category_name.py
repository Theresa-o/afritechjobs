# Generated by Django 4.2.1 on 2023-06-09 13:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('afritechjobsapi', '0022_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
