# Generated by Django 3.0.7 on 2020-06-12 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0016_auto_20200605_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameerror',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='gamelog',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='move',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
