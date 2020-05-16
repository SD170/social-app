# Generated by Django 3.0.5 on 2020-05-04 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0008_friend'),
    ]

    operations = [
        migrations.CreateModel(
            name='FriendList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friends', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='details.Friend')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='details.Profile')),
            ],
        ),
    ]