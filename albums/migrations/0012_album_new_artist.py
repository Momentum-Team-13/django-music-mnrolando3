# Generated by Django 4.0.5 on 2022-07-06 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0011_alter_track_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='new_artist',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
