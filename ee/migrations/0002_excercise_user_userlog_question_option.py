# Generated by Django 4.2.4 on 2023-08-16 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Excercise',
            fields=[
                ('excercise_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=255)),
                ('date_registered', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_completed', models.DateTimeField()),
                ('total_questions', models.IntegerField()),
                ('correct_answers', models.IntegerField()),
                ('excercise_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ee.excercise')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ee.user')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('audio_text', models.CharField(max_length=255)),
                ('excercise_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ee.excercise')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('option_id', models.AutoField(primary_key=True, serialize=False)),
                ('text_option', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField()),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ee.question')),
            ],
        ),
    ]
