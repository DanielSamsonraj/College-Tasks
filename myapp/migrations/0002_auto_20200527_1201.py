# Generated by Django 3.0.3 on 2020-05-27 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='question',
            new_name='question1',
        ),
    ]
