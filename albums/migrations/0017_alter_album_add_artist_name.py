# Generated by Django 4.0.5 on 2022-07-07 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0016_alter_track_track_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='add_artist_name',
            field=models.CharField(max_length=250),
        ),
    ]
