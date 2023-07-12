# Generated by Django 4.2.1 on 2023-07-06 10:29

import afritechjobsapi.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("afritechjobsapi", "0032_remove_postajob_job_level_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="author",
            field=models.ForeignKey(
                default=afritechjobsapi.models.Blog.deleted_author_replacement_default,
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="author",
            field=models.ForeignKey(
                default=afritechjobsapi.models.Event.deleted_author_replacement_default,
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="hiringguide",
            name="author",
            field=models.ForeignKey(
                default=afritechjobsapi.models.HiringGuide.deleted_author_replacement_default,
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="workresources",
            name="author",
            field=models.ForeignKey(
                default=afritechjobsapi.models.WorkResources.deleted_author_replacement_default,
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.DeleteModel(
            name="Profile",
        ),
    ]
