# Generated by Django 3.0.5 on 2020-04-30 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0002_remove_profile_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birth',
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]