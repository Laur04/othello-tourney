# Generated by Django 3.0.6 on 2020-05-22 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_game_ping'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='submitted_time',
            new_name='created_at',
        ),
    ]
