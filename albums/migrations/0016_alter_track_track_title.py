# Generated by Django 4.0.5 on 2022-07-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0015_album_add_artist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='track_title',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
