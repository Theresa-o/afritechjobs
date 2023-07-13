# Generated by Django 4.2.1 on 2023-07-13 12:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0008_alter_user_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("ADMIN", "Admin"),
                    ("RECRUITER", "Recruiter"),
                    ("CANDIDATE", "Candidate"),
                ],
                default="ADMIN",
                max_length=50,
            ),
        ),
    ]
