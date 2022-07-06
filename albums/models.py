# from pyexpat import model
from django.db import models
# from django.core.validators import RegexValidator
# from users.models import User


class Artist(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Album(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,
                               related_name='albums', null=True,
                               blank=True)
    new_artist = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True,
                                      blank=True)
    cover = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class Track(models.Model):
    track_title = models.CharField(max_length=500, null=True, blank=True,
                                   unique=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE,
                              related_name='tracks', null=True,
                              blank=True)

    def __str__(self):
        return f'{self.track_title}'
