# Generated by Django 3.2 on 2023-01-31 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_auto_20230130_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='branch_start',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='branch_tweets', to='tweets.tweet'),
        ),
    ]
