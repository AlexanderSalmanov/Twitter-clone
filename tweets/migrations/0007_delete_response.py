# Generated by Django 3.2.12 on 2022-05-18 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0006_response'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Response',
        ),
    ]