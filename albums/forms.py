from django import forms
from .models import Album, Track, Artist


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'cover',
        ]


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = [
            'name',
        ]


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = [
            'track_title',
        ]
