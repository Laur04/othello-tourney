# Generated by Django 3.0.5 on 2020-04-06 02:37

from django.db import migrations, models
import othello.apps.games.models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='code',
            field=models.FileField(storage=othello.apps.games.models.OverwriteStorage(), upload_to=othello.apps.games.models.save_path),
        ),
    ]