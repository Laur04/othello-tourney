# Generated by Django 3.0.5 on 2020-04-20 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0024_auto_20200419_0255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blackgameerror',
            name='game',
        ),
        migrations.RemoveField(
            model_name='blackgamelog',
            name='game',
        ),
        migrations.RemoveField(
            model_name='blackgamelog',
            name='gamelog_ptr',
        ),
        migrations.DeleteModel(
            name='GameError',
        ),
        migrations.RemoveField(
            model_name='whitegameerror',
            name='game',
        ),
        migrations.RemoveField(
            model_name='whitegamelog',
            name='game',
        ),
        migrations.RemoveField(
            model_name='whitegamelog',
            name='gamelog_ptr',
        ),
        migrations.RemoveField(
            model_name='move',
            name='possible',
        ),
        migrations.DeleteModel(
            name='BlackGameError',
        ),
        migrations.DeleteModel(
            name='BlackGameLog',
        ),
        migrations.DeleteModel(
            name='GameLog',
        ),
        migrations.DeleteModel(
            name='WhiteGameError',
        ),
        migrations.DeleteModel(
            name='WhiteGameLog',
        ),
    ]
