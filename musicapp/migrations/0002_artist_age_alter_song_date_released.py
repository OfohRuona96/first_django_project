# Generated by Django 4.1.2 on 2022-10-27 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='date_released',
            field=models.DateTimeField(),
        ),
    ]
