# Generated by Django 3.2.5 on 2022-06-02 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0018_response'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='sender',
            new_name='author',
        ),
    ]
