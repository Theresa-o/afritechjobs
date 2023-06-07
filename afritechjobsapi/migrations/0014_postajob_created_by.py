# Generated by Django 4.2.1 on 2023-06-07 18:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('afritechjobsapi', '0013_remove_jobskills_user_postajob_date_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='postajob',
            name='created_by',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='afritechjobsapi.profile'),
            preserve_default=False,
        ),
    ]
