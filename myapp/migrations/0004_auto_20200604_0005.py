# Generated by Django 3.0.3 on 2020-06-03 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0003_questions_question_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('question_title', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='questions',
            name='question1',
        ),
        migrations.RemoveField(
            model_name='eachquestion',
            name='correct_option',
        ),
        migrations.RemoveField(
            model_name='eachquestion',
            name='question',
        ),
        migrations.AddField(
            model_name='eachquestion',
            name='correctOption',
            field=models.CharField(default=None, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eachquestion',
            name='question_name',
            field=models.TextField(default='inactive', max_length=300),
        ),
        migrations.AlterField(
            model_name='eachquestion',
            name='option1',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='eachquestion',
            name='option2',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='eachquestion',
            name='option3',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='eachquestion',
            name='option4',
            field=models.CharField(max_length=30),
        ),
        migrations.DeleteModel(
            name='Exam',
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
        migrations.AddField(
            model_name='question',
            name='user_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.EachQuestion'),
        ),
    ]
