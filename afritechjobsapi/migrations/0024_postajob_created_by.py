# Generated by Django 4.2.1 on 2023-06-09 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('afritechjobsapi', '0023_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='postajob',
            name='created_by',
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to='afritechjobsapi.profile'
            ),
            preserve_default=False,
        ),
    ]
