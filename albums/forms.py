from django import forms
from .models import Album, Track


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'title',
            'artist',
            'cover',
        ]


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = [
            'track_title',
        ]
