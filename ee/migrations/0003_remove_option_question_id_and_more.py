# Generated by Django 4.2.4 on 2023-08-24 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ee', '0002_userlog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='question_id',
        ),
        migrations.RemoveField(
            model_name='question',
            name='excercise_id',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.DeleteModel(
            name='Excercise',
        ),
        migrations.DeleteModel(
            name='Option',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
