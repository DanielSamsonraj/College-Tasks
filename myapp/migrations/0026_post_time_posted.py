# Generated by Django 3.0.3 on 2020-06-30 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0025_post_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='time_posted',
            field=models.TimeField(auto_now=True),
        ),
    ]
