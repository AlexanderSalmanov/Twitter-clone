# Generated by Django 3.2.12 on 2022-05-07 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_remove_profile_tweets'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='nickname',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]
