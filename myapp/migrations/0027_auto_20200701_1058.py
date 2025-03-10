# Generated by Django 3.0.3 on 2020-07-01 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_post_time_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='branch',
            field=models.CharField(choices=[('GlOBAL', 'GLOBAL'), ('CSE', 'CSE'), ('MECH', 'MECH'), ('EEE', 'EEE'), ('ECE', 'ECE'), ('IT', 'IT'), ('CIVIL', 'CIVIL'), ('ECM', 'ECM')], default='GlOBAL', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='sections',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='All Years', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='year',
            field=models.CharField(choices=[('All Years', 'All Years'), ('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV')], default='All Years', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='year',
            field=models.CharField(choices=[('All Years', 'All Years'), ('I', 'I'), ('II', 'II'), ('III', 'III'), ('IV', 'IV')], default='I', max_length=20),
        ),
    ]
