# Generated by Django 3.2.6 on 2021-09-01 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='skills',
        ),
    ]