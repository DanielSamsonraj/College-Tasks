# Generated by Django 3.0.3 on 2020-06-30 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_auto_20200630_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
