import os
from django.contrib import admin
from .models import Album, Song


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('uploaded_by', 'artist', 'album_name')
    list_filter = ('uploaded_by', 'artist', 'date_uploaded', 'genre')
    search_field = ('album_name', 'artist')
    prepopulated_fields = {'slug': ('album_name',)}


admin.site.register(Album, AlbumAdmin)


class SongAdmin(admin.ModelAdmin):
    list_display = ('album', 'song_title', 'audio_file')
    prepopulated_fields = {'slug': ('song_title',)}


admin.site.register(Song, SongAdmin)
