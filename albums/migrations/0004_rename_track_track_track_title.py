# Generated by Django 4.0.5 on 2022-07-03 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_track'),
    ]

    operations = [
        migrations.RenameField(
            model_name='track',
            old_name='track',
            new_name='track_title',
        ),
    ]
