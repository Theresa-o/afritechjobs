# Generated by Django 4.2.1 on 2023-07-27 11:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0012_random_alter_user_role"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Random",
        ),
    ]