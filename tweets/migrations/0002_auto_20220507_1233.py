# Generated by Django 3.2.12 on 2022-05-07 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_remove_profile_tweets'),
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='user',
        ),
        migrations.AddField(
            model_name='tweet',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.CharField(default='', max_length=140),
        ),
    ]
