# Generated by Django 5.1.3 on 2025-01-02 03:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]
