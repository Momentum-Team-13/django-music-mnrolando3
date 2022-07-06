# Generated by Django 4.0.5 on 2022-07-06 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0009_alter_artist_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='album',
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='albums.artist'),
        ),
    ]
