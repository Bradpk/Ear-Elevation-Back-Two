# Generated by Django 4.2.4 on 2023-08-24 03:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('exercise_id', models.CharField(max_length=100)),
                ('date_completed', models.CharField(max_length=100)),
                ('total_questions', models.CharField(max_length=100)),
                ('correct_answers', models.CharField(max_length=100)),
                ('percentage_correct', models.CharField(max_length=200)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]