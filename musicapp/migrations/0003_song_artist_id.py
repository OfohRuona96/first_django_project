# Generated by Django 4.1.2 on 2022-10-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0002_lyric_song_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artist_id',
            field=models.IntegerField(default=''),
            preserve_default=False,
        ),
    ]
