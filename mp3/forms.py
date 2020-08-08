from cloudinary.forms import CloudinaryJsFileField
from django import forms

from .models import Album, Song


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['artist', 'album_name', 'genre', 'album_logo']


class SongForm(forms.ModelForm):
    # audio_file = CloudinaryJsFileField()
    # album_key = forms.CharField()
    class Meta:
        model = Song
        fields = ['song_title', 'price']
